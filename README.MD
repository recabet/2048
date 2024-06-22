# 2048 Game using Pygame

This project implements the classic 2048 game using Pygame, a popular Python library for game development. The game involves combining tiles with the same number to reach the tile with the number 2048.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

2048 is a single-player sliding block puzzle game developed by Gabriele Cirulli. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. This implementation uses Pygame to create a graphical interface and handle user input.

## Installation

To run the 2048 game:

1. Clone the repository: git clone <https://github/recabet/2048>

2. Navigate to the project directory: cd 2048

3. Install Pygame if not already installed: pip install pygame

4. Run the game: python 2048.py


## Usage

- Use the arrow keys (Up, Down, Left, Right) to move tiles on the grid.
- Tiles with the same number merge into one when they collide.
- After each move, a new tile appears randomly on an empty spot with a value of either 2 or 4.
- The goal is to create a tile with the number 2048.
- The game ends when no more moves can be made.

## Gameplay

- **Grid Size**: The game grid is 4x4 by default.
- **Tile Colors**: Tiles have different colors based on their value, following a predefined color scheme.
- **Losing Condition**: The game ends when no more moves can be made and no empty spots are available.

## Functions

### `add_new_tile()`

Generates a new tile (either 2 or 4) in a random empty cell on the grid.

### `draw_grid()`

Draws the game grid on the Pygame screen, including tiles with their respective numbers and colors.

### `move_tiles_left()`

Moves all tiles to the left in the grid, merging adjacent tiles with the same number if they collide. Returns the updated grid and a boolean indicating if any tiles were moved.

### `rotate_grid_clockwise(grid)`

Rotates the given grid clockwise by 90 degrees.

### `rotate_grid_counterclockwise(grid)`

Rotates the given grid counterclockwise by 90 degrees.

### `move(direction)`

Moves tiles on the grid based on the specified direction ('left', 'right', 'up', 'down'). Updates the grid and returns a boolean indicating if any tiles were moved.

### `can_move()`

Checks if there are any possible moves left on the grid. Returns `True` if at least one tile can be moved, `False` otherwise.

### `handle_input()`

Handles user input events (key presses). Moves tiles on the grid accordingly (left, right, up, down) and adds a new tile if a move was made. Returns `True` if the game can continue, `False` if the game is over.

### `show_lose_message()`

Displays a "You Lose!" message on the Pygame screen when the game ends. Pauses the game for 2 seconds before quitting.

### `main()`

Main game loop that initializes the game, handles game events, updates the screen, and checks game over conditions. Exits the game loop and displays a lose message when the game ends.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature`)
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request.

Please ensure that your code follows the existing coding style and conventions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



