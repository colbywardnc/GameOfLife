# Game of Life

A Python implementation of Conway's Game of Life built with Tkinter.

## Features

- Interactive 20x20 game board
- Click cells to make them alive or dead
- Step through generations manually
- Start & pause the simulation
- Reset the board
- Adjustable simulation speed
- Generation counter
- Implements Conway's Game of Life rules from scratch

## How to Run

1. Make sure Python is installed.
2. Clone this repository.
3. Open the project in PyCharm or another Python IDE.
4. Run `main.py`.

## How it Works

The game uses a grid of cells where each cell is either alive or dead. Each generation checks the eight cells surrounding every cell and applies the standard Game of Life rules.

## Rules

- A living cell with 2 or 3 neighbors survives.
- A living cell with fewer than 2 neighbors dies.
- A living cell with more than 3 neighbors dies.
- A dead cell with exactly 3 neighbors becomes alive.

## Files

- `main.py` - Handles the graphical interface and user controls.
- `game.py` - Contains the Game of Life logic.
- `.gitignore` - Prevents unnecessary files from being committed.

## Technologies

- Python
- Tkinter
- Git/GitHub