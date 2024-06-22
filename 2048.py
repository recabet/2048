import pygame as pg
import random
import sys


pg.init()


GRID_SIZE = 4
TILE_SIZE = 100
GRID_MARGIN = 10
WINDOW_SIZE = (GRID_SIZE * (TILE_SIZE + GRID_MARGIN) + GRID_MARGIN,
               GRID_SIZE * (TILE_SIZE + GRID_MARGIN) + GRID_MARGIN)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
LARGE_FONT_SIZE = 72


screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('2048 Game')


font = pg.font.Font(None, FONT_SIZE)
large_font = pg.font.Font(None, LARGE_FONT_SIZE)


COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}


grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def add_new_tile():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4

def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            tile_value = grid[i][j]
            color = COLORS.get(tile_value, (205, 193, 180))
            pg.draw.rect(screen, color,
                         (GRID_MARGIN + j * (TILE_SIZE + GRID_MARGIN),
                          GRID_MARGIN + i * (TILE_SIZE + GRID_MARGIN),
                          TILE_SIZE, TILE_SIZE))
            if tile_value != 0:
                text_surface = font.render(str(tile_value), True, BLACK)
                text_rect = text_surface.get_rect(center=(GRID_MARGIN + j * (TILE_SIZE + GRID_MARGIN) + TILE_SIZE / 2,
                                                          GRID_MARGIN + i * (TILE_SIZE + GRID_MARGIN) + TILE_SIZE / 2))
                screen.blit(text_surface, text_rect)

def move_tiles_left():
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    moved = False
    for i in range(GRID_SIZE):
        current_row = [tile for tile in grid[i] if tile != 0]
        j = 0
        while j < len(current_row) - 1:
            if current_row[j] == current_row[j + 1]:
                current_row[j] *= 2
                current_row[j + 1] = 0
                moved = True
            j += 1
        current_row = [tile for tile in current_row if tile != 0]
        if current_row != grid[i][:len(current_row)]:
            moved = True
        new_grid[i][:len(current_row)] = current_row
    return new_grid, moved

def rotate_grid_clockwise(grid):
    return [list(row) for row in zip(*grid[::-1])]

def rotate_grid_counterclockwise(grid):
    return [list(row) for row in zip(*grid)][::-1]

def move(direction):
    global grid
    moved = False
    if direction == 'left':
        new_grid, moved = move_tiles_left()
    elif direction == 'right':
        grid = [row[::-1] for row in grid]
        new_grid, moved = move_tiles_left()
        new_grid = [row[::-1] for row in new_grid]
    elif direction == 'up':
        grid = rotate_grid_counterclockwise(grid)
        new_grid, moved = move_tiles_left()
        new_grid = rotate_grid_clockwise(new_grid)
    elif direction == 'down':
        grid = rotate_grid_clockwise(grid)
        new_grid, moved = move_tiles_left()
        new_grid = rotate_grid_counterclockwise(new_grid)
    grid = new_grid
    return moved

def can_move():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return True
            if j < GRID_SIZE - 1 and grid[i][j] == grid[i][j + 1]:
                return True
            if i < GRID_SIZE - 1 and grid[i][j] == grid[i + 1][j]:
                return True
    return False

def handle_input():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            moved = False
            if event.key == pg.K_LEFT:
                moved = move('left')
            elif event.key == pg.K_RIGHT:
                moved = move('right')
            elif event.key == pg.K_UP:
                moved = move('up')
            elif event.key == pg.K_DOWN:
                moved = move('down')
            if moved:
                add_new_tile()
            if not can_move():
                return False
    return True

def show_lose_message():
    lose_surface = large_font.render("You Lose!", True, (255, 0, 0))
    lose_rect = lose_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    screen.blit(lose_surface, lose_rect)
    pg.display.update()
    pg.time.wait(2000)

def main():
    add_new_tile()
    add_new_tile()
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()
        pg.display.update()
        running = handle_input()
        if not running:
            show_lose_message()
            pg.quit()
            sys.exit()

if __name__ == '__main__':
    main()
