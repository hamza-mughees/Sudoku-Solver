from sudoku_solver import Sudoku
from button import Button
import pygame

pygame.init()

win_width = 450
win_height = 500

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Sudoku Solver")

cell_width = win_width//9
bg = (255, 255, 255)
fg = (0, 0, 0)
font = pygame.font.Font(None, 32)

grid = [
    ['9', '0', '6', '0', '7', '0', '4', '0', '3'],
    ['0', '0', '0', '4', '0', '0', '2', '0', '0'],
    ['0', '7', '0', '0', '2', '3', '0', '1', '0'],
    ['5', '0', '0', '0', '0', '0', '1', '0', '0'],
    ['0', '4', '0', '2', '0', '8', '0', '6', '0'],
    ['0', '0', '3', '0', '0', '0', '0', '0', '5'],
    ['0', '3', '0', '7', '0', '0', '0', '5', '0'],
    ['0', '0', '7', '0', '0', '5', '0', '0', '0'],
    ['4', '0', '5', '0', '1', '0', '7', '0', '8'],
]

def horiz_line(y, t):
    pygame.draw.line(
        win, 
        fg, 
        (0, y), 
        (9*cell_width, y), 
        t,
    )

def vert_line(x, t):
    pygame.draw.line(
        win, 
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
            win, 
            bg, 
            cell,
        )
        num_disp = font.render(
            str(num_in_cell), 
            True, 
            fg,
        )
        win.blit(
            num_disp, 
            (cell.x + 15, cell.y + 10),
        )

a_cell_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed_pos = event.pos
            if mouse_pressed_pos[1] <= 450:
                a_cell_active = True
            if solve_button.mouse_is_over(mouse_pressed_pos):
                grid = [list(map(int, row)) for row in grid]
                puzzle = Sudoku(grid)
                puzzle.solve()
                solutions = puzzle.get_solutions()
                grid = solutions[0] if len(solutions) > 0 else grid
                grid = [list(map(str, row)) for row in grid]
            
        if event.type == pygame.KEYDOWN:
            if a_cell_active:
                if event.unicode >= '0' and event.unicode <= '9': 
                    grid[i][j] = grid[i][j][:-1]
                    grid[i][j] += event.unicode
                if event.key == pygame.K_RETURN:
                    a_cell_active = False
    
    win.fill(bg)

    for i in range(10):
        if i % 3 == 0: t = 4
        else: t = 1
        horiz_line(i*cell_width, t)
        vert_line(i*cell_width, t)
    
    for i in range(9):          # to display all cells
        for j in range(9):
            update_cell(i, j)
    
    if a_cell_active and mouse_pressed_pos[1] <= 450:    # to update and display active cell
        i = mouse_pressed_pos[1] // cell_width
        j = mouse_pressed_pos[0] // cell_width
        update_cell(i, j)
    
    solve_button = Button(15, 465, 60, 24, bg, "Solve")
    solve_button.draw(win, True)
    
    pygame.display.update()
