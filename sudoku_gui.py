from sudoku_solver import Sudoku
import pygame

pygame.init()

screen_width = 450
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Solver")

cell_width = screen_width//9
bg = (255, 255, 255)
fg = (0, 0, 0)
base_font = pygame.font.Font(None, 32)

grid = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
]

def horiz_line(y, t):
    pygame.draw.line(
        screen, 
        fg, 
        (0, y), 
        (9*cell_width, y), 
        t,
    )

def vert_line(x, t):
    pygame.draw.line(
        screen, 
        fg, 
        (x, 0), 
        (x, 9*cell_width), 
        t,
    )

def update_cell(i, j):
    nw_offset = 4
    se_offset = -6
    num_in_cell = grid[i][j]
    if num_in_cell != '0':
        cell = pygame.Rect(
            j*cell_width + nw_offset, 
            i*cell_width + nw_offset, 
            cell_width + se_offset, 
            cell_width + se_offset,
        )
        pygame.draw.rect(
            screen, 
            bg, 
            cell,
        )
        num_disp = base_font.render(
            num_in_cell, 
            True, 
            fg,
        )
        screen.blit(
            num_disp, 
            (cell.x + 15, cell.y + 10),
        )

a_cell_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            a_cell_active = True
            mouse_pressed_pos = event.pos
        if event.type == pygame.KEYDOWN:
            if a_cell_active:
                if event.unicode >= '0' and event.unicode <= '9': 
                    grid[i][j] = grid[i][j][:-1]
                    grid[i][j] += event.unicode
                if event.key == pygame.K_RETURN:
                    a_cell_active = False
    
    screen.fill(bg)

    for i in range(10):
        if i % 3 == 0: t = 4
        else: t = 1
        horiz_line(i*cell_width, t)
        vert_line(i*cell_width, t)
    
    for i in range(9):          # to display all cells
        for j in range(9):
            update_cell(i, j)
    
    if a_cell_active and mouse_pressed_pos[1] < 450:    # to update and display active cell
        i = mouse_pressed_pos[1] // cell_width
        j = mouse_pressed_pos[0] // cell_width
        update_cell(i, j)
    
    pygame.display.update()
