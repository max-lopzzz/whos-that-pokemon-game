# Who's That Pokémon? Game (Version 2.0) 🎮✨
**Who's That Pokémon?** is an enhanced, Python-based quiz game that challenges players to guess Pokémon from images. Built with Streamlit, CSV, and PIL, this version offers an interactive and engaging experience.

## About the Game 🐾
**"Who's That Pokémon?"** is a fun and interactive game that tests your knowledge of Pokémon. Inspired by the classic segment from the Pokémon anime, this game challenges players to identify Pokémon based on their images. Featuring **all 1215 Pokémon** from the Pokédex, it’s an excellent way to see how well you know your favorite Pokémon!

## Features 🌟
- **Random Pokémon Selection:** Randomly selects a Pokémon from the entire Pokédex for each round.
- **Streamlit Interface:** User-friendly web interface that is easy to navigate.
- **Dynamic Pokémon Images:** Displays Pokémon images for you to guess.
- **Score Tracking:** Keeps track of your current and maximum score.
- **Victory Screen:** Celebrates your success when you correctly guess all Pokémon! 🏆
- **Error Feedback:** Provides the correct answer when you make a mistake and allows you to try again. ❌➡️✅

## Gameplay 🎉
- Click **"Start Game"** to begin.
- A Pokémon image will appear on screen.
- Type your guess in the text box and press **Enter**.
- If you’re correct, you'll move on to the next Pokémon! ✅
- If you’re incorrect, you'll see an error screen with the correct answer and your score, allowing you to try again. 🔄

## Installation 🛠️
### Prerequisites
Ensure you have Python 3 installed along with the following packages:
- `Streamlit` for the web interface.
- `Pillow` (PIL) for image handling
- `csv` (standard library)
- `random` (standard library)
You can install the required packages using the provided `requirements.txt` file:
```
pip install -r requirements.txt
```
### Clone the repository
Clone the repository to your local machine using:
```
git clone https://github.com/yourusername/whos-that-pokemon-game2.git
```
### Run the game
Navigate to the repository folder and run the game:
```
cd whos-that-pokemon-game
streamlit run pokemon_game2.py
```

## Demo Video 🎥
Watch the demo of "Who's That Pokémon?" here: [Demo Video](demo.mp4)

## File Structure
- `pokemon_game2.py`: Main game script.
- `pokedex.csv`: CSV file containing Pokémon data.
- `images/`: Directory containing Pokémon images.
- `demo.mp4`: Directory containing the demo video. 

## How it Works 🔍
- `pokedex.csv`: The game reads from pokedex.csv to load Pokémon names and image paths.
- `Streamlit GUI`: Utilizes Streamlit to create a simple and interactive web interface.
- `Random Selection`: A random Pokémon is chosen for each round.
- `Victory & Error Screens`: Displays different screens based on whether your guess is correct or not.

## Contributing 🤝
Contributions are welcome! If you have ideas for improvements or find any bugs, please feel free to:
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add a new feature'`).
- Push to the branch (`git push origin feature-branch`).
- Create a **Pull Request**.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Aknowledgements 🙏
- Pokémon images and data used in this game are the property of The Pokémon Company and Nintendo. This is a fan-made project for educational and entertainment purposes.
- Inspired by the original "Who's That Pokémon?" from the Pokémon anime series.

## Credits 🏆
- **CSV Data:** `pokedex.csv` and `images` were sourced from [Kaggle: Pokemon with stats and image](https://www.kaggle.com/datasets/christofferms/pokemon-with-stats-and-image).

## Contact 📫
Feel free to contact me via GitHub or open an issue if you encounter any problems or have questions.

Happy guessing, and may you catch 'em all! 🎉
