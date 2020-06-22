import pygame
pygame.init()

wnd_size = 450
wnd = pygame.display.set_mode((wnd_size, wnd_size))
pygame.display.set_caption("Sudoku Solver")

cell_size = wnd_size//9
box_size = cell_size*3
bg = (0, 0, 0)
fg = (255, 255, 255)

def horiz_line(y, t):
    pygame.draw.line(wnd, fg, (0, y), (wnd_size, y), t)

def vert_line(x, t):
    pygame.draw.line(wnd, fg, (x, 0), (x, wnd_size), t)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    wnd.fill(bg)

    for i in range(1, 9):
        if i == 3 or i == 6: t = 4
        else: t = 1
        horiz_line(i*cell_size, t)
        vert_line(i*cell_size, t)
    
    pygame.display.update()

pygame.quit()
