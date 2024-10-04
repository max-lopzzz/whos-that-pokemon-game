import tkinter as tk
import csv
import random
from PIL import Image, ImageTk

# Existing variables and game state
pokedex = []
current_score = 0
max_score = 0
current_pokemon = None

# Load pokedex data from CSV
with open('pokedex.csv', 'r') as file:
    reader = csv.reader(file)
    pokedex = list(reader)

# Function to load random Pokémon
def load_random_pokemon():
    pokemon = random.choice(pokedex)
    return pokemon[0], pokemon[2]  

# Function to verify user's answer
def verify_answer():
    answer = name_entry.get().strip().lower()
    global current_score

    answer_words = answer.split()
    pokemon_words = current_pokemon.lower().split()

    correct = any(word in pokemon_words for word in answer_words)

    if correct:
        current_score += 1
        if current_score == 1025:
            show_victory_screen()
        else:
            next_pokemon()
    else:
        show_error_screen()

# Function to load the next Pokémon
def next_pokemon():
    global pokemon_image, current_pokemon
    image_path, current_pokemon = load_random_pokemon()

    img = Image.open(image_path)
    img = img.resize((500, 500))
    pokemon_image = ImageTk.PhotoImage(img)

    image_label.config(image=pokemon_image)
    name_entry.delete(0, tk.END)

# Start game
def start_game():
    start_screen.pack_forget()
    show_game_screen()

# Show the game screen
def show_game_screen():
    game_screen.pack()
    next_pokemon()

# Show error screen
def show_error_screen():
    global max_score, current_score
    game_screen.pack_forget()

    if current_score > max_score:
        max_score = current_score

    score_label.config(text=f"Current Score: {current_score}")
    max_score_label.config(text=f"Max Score: {max_score}")
    correct_answer_label.config(text=f"The correct answer was: {current_pokemon}")
    
    error_screen.pack()

# Reset game after error or victory
def reset_game():
    global current_score
    current_score = 0
    error_screen.pack_forget()
    victory_screen.pack_forget()
    next_pokemon()
    game_screen.pack()

# Show the victory screen
def show_victory_screen():
    game_screen.pack_forget()
    victory_screen.pack()

# Tkinter root setup
root = tk.Tk()
root.title("Who's That Pokémon?")
root.geometry("1000x1000")

# Start screen setup
start_screen = tk.Frame(root)
start_screen.pack()

title = tk.Label(start_screen, text="Who's That Pokémon?", font=("Pokemon Classic", 24))
title.pack(pady=20)

start_button = tk.Button(start_screen, text="Start Game", command=start_game, font=("Pokemon Classic", 16))
start_button.pack(pady=20)

# Game screen setup
game_screen = tk.Frame(root)

instruction_label = tk.Label(game_screen, text="Who's this Pokémon?", font=("Pokemon Classic", 20))
instruction_label.pack(pady=20)

pokemon_image = None
image_label = tk.Label(game_screen)
image_label.pack()

name_entry = tk.Entry(game_screen, font=("Pokemon Classic", 16))
name_entry.pack(pady=10)

verify_button = tk.Button(game_screen, text="Verify", command=verify_answer, font=("Pokemon Classic", 16))
verify_button.pack(pady=10)

# Error screen setup
error_screen = tk.Frame(root)

error_label = tk.Label(error_screen, text="You got it wrong!", font=("Pokemon Classic", 24))
error_label.pack(pady=20)

score_label = tk.Label(error_screen, text=f"Current Score: {current_score}", font=("Pokemon Classic", 16))
score_label.pack(pady=10)

max_score_label = tk.Label(error_screen, text=f"Max Score: {max_score}", font=("Pokemon Classic", 16))
max_score_label.pack(pady=10)

correct_answer_label = tk.Label(error_screen, text="", font=("Pokemon Classic", 16))
correct_answer_label.pack(pady=10)

reset_button = tk.Button(error_screen, text="Play Again", command=reset_game, font=("Pokemon Classic", 16))
reset_button.pack(pady=20)

# Victory screen setup
victory_screen = tk.Frame(root)

victory_label = tk.Label(victory_screen, text="Congratulations! You guessed all 1025 Pokémon", font=("Pokemon Classic", 24))
victory_label.pack(pady=20)

reset_button_victory = tk.Button(victory_screen, text="Play Again", command=reset_game, font=("Pokemon Classic", 16))
reset_button_victory.pack(pady=20)

# Start Tkinter mainloop
root.mainloop()
