import streamlit as st
from PIL import Image
import random
import csv

# Load the Pokedex data from the CSV file
pokedex = []
with open('pokedex.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    pokedex = list(reader)

# Function to load a random Pokémon
def load_random_pokemon():
    pokemon = random.choice(pokedex)
    return pokemon[0], pokemon[2]  # Returning image path and name

# Function to verify the answer
def verify_answer(user_guess, current_pokemon):
    answer = user_guess.strip().lower()
    answer_words = answer.split()
    pokemon_words = current_pokemon.lower().split()
    return any(word in pokemon_words for word in answer_words)

# Function to handle user guess submission
def submit():
    current_pokemon_name = st.session_state['current_pokemon_name']
    user_guess = st.session_state['user_guess'].strip().lower()

    if verify_answer(user_guess, current_pokemon_name):
        st.success(f"Correct! It's {current_pokemon_name}!")
        st.session_state.current_score += 1
        if st.session_state.current_score > st.session_state.max_score:
            st.session_state.max_score = st.session_state.current_score

        # Check for victory condition
        if st.session_state.current_score == 1215:
            st.session_state.game_state = "victory"
        else:
            load_new_pokemon()  # Load a new Pokémon if not victorious
    else:
        st.session_state.game_state = "game_over"
        st.session_state.correct_answer = current_pokemon_name  # Store the correct answer
        st.session_state.current_score = 0

# Function to load a new Pokémon
def load_new_pokemon():
    image_path, pokemon_name = load_random_pokemon()
    st.session_state['current_pokemon_name'] = pokemon_name
    st.session_state['current_image_path'] = image_path
    st.session_state['user_guess'] = ""  # Clear the text input

# Function to start the game
def start_game():
    st.session_state.game_state = "playing"
    load_new_pokemon()  # Load the first Pokémon immediately

# Function to reset the game (used for "Try Again" and "Play Again")
def reset_game():
    st.session_state.current_score = 0
    st.session_state.game_state = "start"
    st.session_state.pop('current_image_path', None)  # Remove current image path if it exists
    st.session_state.pop('current_pokemon_name', None)  # Remove current Pokémon name if it exists
    st.session_state.pop('correct_answer', None)  # Clear stored correct answer

# Initialize game state
if 'game_state' not in st.session_state:
    st.session_state.game_state = "start"
if 'current_score' not in st.session_state:
    st.session_state.current_score = 0
if 'max_score' not in st.session_state:
    st.session_state.max_score = 0

# Streamlit app code
st.title("Who's that Pokémon? 2.0")

# Start Screen
if st.session_state.game_state == "start":
    st.write("Welcome to 'Who's that Pokémon!' Can you guess all the Pokémon?")
    if st.button("Start Game", on_click=start_game):
        pass  # The game state will be updated by start_game function

# Victory Screen
elif st.session_state.game_state == "victory":
    st.success("Congratulations! You guessed all 1215 Pokémon correctly!")
    if st.button("Play Again", on_click=reset_game):
        pass  # The game state will be updated by reset_game function

# Game Over Screen
elif st.session_state.game_state == "game_over":
    correct_answer = st.session_state.get('correct_answer', "unknown")
    st.error(f"The correct answer was: {correct_answer}")
    st.error("Game Over! Better luck next time.")
    st.write(f"Max Score Achieved: {st.session_state.max_score}")
    if st.button("Try Again", on_click=reset_game):
        pass  # The game state will be updated by reset_game function

# Main Game Screen
elif st.session_state.game_state == "playing":
    if 'current_image_path' in st.session_state:
        # Display the current Pokémon
        st.image(st.session_state['current_image_path'], caption="Who's that Pokémon?", use_column_width='never')

        # Text input for guessing the Pokémon's name
        st.text_input("Enter the Pokémon's name:", key="user_guess", on_change=submit)

    # Display the current and maximum scores
    st.write(f"Current Score: {st.session_state.current_score}")
    st.write(f"Max Score: {st.session_state.max_score}")
