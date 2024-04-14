## NOTE: Complete rework in progress! Moving to new repository!
when working on some of th new features, i have had so many ideas the the entire structure of the code needs to be entirely rewritten. plus some of the code is pretty bad and i've learned a lot since beginning this project. 
ive also come up with a name. Quest Engine!
since the project is changing so drasticly though, i thought it would be bettter to just make a completely new repository and a completely new project. i'll definitely be making more regular commits and update the changelog so you can keep track of the changes. the new repo will be `levgrav/quest-engine`. be sure to follow over there. Ill be leaving this one here for myelf to look back on and laugh, plus it's a good proof of concept.

# Text RPG Game Engine

Version: 0.6.0 - AI update

This repository contains a game engine for a text-based RPG, written in Python. The game is mainly command-line based, but it also includes support for a GUI using Tkinter. Most game-specific information is stored in JSON files.

Keep in mind this is an early version and a work in progress. It is not currently entirely functional. Currently, the game engine is more of an interactive world engine, and less a game.

## Features
- A flexible command system that allows players to interact with the game world using natural language commands
- A robust system for managing game objects, including NPCs, items, and locations
- The ability to customize the game world using JSON files
- Command line & GUI capabilities
- Packaged in a nice executable file
- The option to save and load game progress
- Transformer (GPT) based command parser and Describer

### Planned Features
- Ability to export games as executables
- Quests, Combat, NPC interaction (After this, it will have an actual win condition and will be released as alpha version 1.0.0)
- AI-assisted world generation and npc controller
- UI features for easy world creation and game editing

## Requirements

- Python 3

### Dependencies
- PySimpleGUI (GUI)
- Art (command line)
- openai (GPT)

## Usage

To use the game engine, clone this repository.

`git clone https://github.com/levgrav/text-rpg.git
cd rpg-game-engine`

To customize the game, edit the JSON files in the `game_data` directory.

To run the game, run the `main.py` file:

`python main.py`

If you want to use the GUI, in `game_data/settings.json`, make sure it says, `"io_outlet": "gui"` instead of `"io_outlet": "terminal"` and vice versa for those that want a command-line game. Likewise, if you want to use the GhatGPT parser, make sure it says, `"parser_type": "gpt"` instead of `"parser_type": "standard"` and vice versa for those that want a standard parser.
Note: if you want to use GPT for the parser and NPC chatbot, you will (as of yet) need to provide your own API key. I may be able to get a public version running, but it might rely on ads or donations. I hate ads though.

## Game World

The informaion about the game world is located in `default_world.json`. All of the information is categorized into `"areas": [...]` and `"npcs": [...]`. In python that will look like `World.areas` and `World.npcs` which will each be a list of `Area` and `Npc` objects, respectively. 

The game map is divided in a grid, each cell being an `Area`. Each `Area` is further subdivided into `Room`s (both if which the player can enter)

### Areas

`Area` objects contains the information needed for a section of the world map. 

Attributes:
- name
    - `str` object that contains the name of the area.
- pos
    - `list` object that contains the position of the area in the form `[x, y]`
- description
    - `str` object that contains a brief description of the area.
- rooms
    - `list` object that contains `Room` objects (see below for a more detailed description).
- containers
    - `list` object that contains `Container` objects (see below for a more detailed description).
- inventory
    - `list` object that contains `Item` objects (see below for a more detailed description).


### Rooms

`Room` objects contains the information needed for a room (duh). Rooms are located inside areas and can all be accessed from anywhere inside their respective area. 

Attributes:
- name
    - `str` object that contains the name of the room.
- description
    - `str` object that contains a brief description of the area.
- containers
    - `list` object that contains `Container` objects (see below for a more detailed description).
- inventory
    - `list` object that contains `Item` objects (see below for a more detailed description).

### Containers

`Container` objects contains information (such as container inventory) for a container. Containers can exist both in `Area`s and `Room`s

Attributes:
- name
    - `str` object that contains the name of the area.
- description
    - `str` object that contains a brief description of the area.
- inventory
    - `list` object that contains `Item` objects (see below for a more detailed description).

### Items
Items contain item-spcific information that is unique to each item type. For example a `Melee_Weapon` might have an attribute `base_damage`.

Some attributes all items have in commom:
- name
    - `str` object that contains the name of the item.
- description
    - `str` object that contains a brief description of the item.
- item_type
    - `str` object that contains the type of item, such as `'Melee_Weapon'` or `'Food'`. 

## Lisence

MIT License (c) 2023 Levi Eby. See `LICENSE.md` for more details.

## Credits

This game engine was (and is currently being) developed by Levi Eby.
