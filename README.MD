2048 Game

This is a simple implementation of the popular 2048 game using Pygame. The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. You can continue to play even after reaching the 2048 tile to achieve higher scores.

Features
Basic 2048 gameplay with tiles that merge when moved in the same direction.
Supports movement in all four directions: left, right, up, and down.
Automatic addition of new tiles after each move.
Detects and handles the losing condition, displaying a "You Lose" message with an animation.
Installation
Ensure you have Python installed. You can download it from python.org.

Install Pygame using pip:


pip install pygame

Download the script and save it to a file, for example, 2048.py.

Usage

Run the game script using Python:

python 2048.py

Use the arrow keys to move the tiles:

Left Arrow: Move tiles left
Right Arrow: Move tiles right
Up Arrow: Move tiles up
Down Arrow: Move tiles down
When no moves are possible, the game will display a "You Lose" message and exit after a short delay.

Code Explanation
Main Components
Game Initialization: Initializes the game window and sets up the initial grid.
Tile Management: Handles adding new tiles and merging tiles based on user input.
Drawing Functions: Renders the grid and tiles on the screen.
Movement Handling: Moves tiles in the specified direction and checks for possible moves.
Losing Condition: Checks if no moves are possible and displays the "You Lose" message.
Functions
add_new_tile(): Adds a new tile (2 or 4) at a random empty position on the grid.
draw_grid(): Draws the grid and tiles on the screen.
move_tiles_left(): Handles merging and moving tiles to the left.
rotate_grid_clockwise(grid): Rotates the grid clockwise.
rotate_grid_counterclockwise(grid): Rotates the grid counterclockwise.
move(direction): Moves tiles in the specified direction.
can_move(): Checks if there are any valid moves left.
handle_input(): Processes user input and updates the game state.
show_lose_message(): Displays the "You Lose" message with an animation.
Acknowledgments
This implementation is inspired by the original 2048 game by Gabriele Cirulli. You can find the original game here.

License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code as you wish.