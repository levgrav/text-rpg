# RPG Game Engine

Version: 0.2.0

This repository contains a game engine for a text-based RPG, written in Python. The game is mainly command-line based, but it also includes support for a GUI using Tkinter. Most game-specific information is stored in JSON files.

Keep in mind this is an early version and a work in progress. It is not currently functional.

## Features

- A flexible command system that allows players to interact with the game world using natural language commands
- A robust system for managing game objects, including NPCs*, items, and locations
- The option to save and load game progress*
- The ability to customize the game world using JSON files

*Incomplete

## Requirements

- Python 3.6 or later
- Tkinter (GUI)
- Art (command line)

## Usage

To run the game, clone this repository and run the `main.py` file:

`git clone https://github.com/[YOUR_USERNAME]/rpg-game-engine.git
cd rpg-game-engine
python main.py`

If you want to use the GUI, you can add the parameter `'gui'` in `command_center.main_menu()` in line 9 in `main` in `main.py` 

To customize the game world, edit the JSON files in the `game_data` directory.

## Credits

This game engine was (and is currently being) developed by Levi Eby.
