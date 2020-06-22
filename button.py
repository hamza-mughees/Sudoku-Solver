import pygame

class Button:
    def __init__(self, x, y, width, height, colour, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
    
    def draw(self, surface, border=False):
        if border:
            pygame.draw.rect(
                surface,
                border,
                (self.x-2, self.y-2, self.width+4, self.height+4),
                0,
            )
        pygame.draw.rect(
            surface,
            self.colour,
            (self.x, self.y, self.width, self.height),
            0,
        )

        if self.text != '':
            font = pygame.font.Font(None, 20)
            text = font.render(
                self.text, 
                True, 
                (0, 0, 0)
            )
            surface.blit(
                text, 
                (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2))
            )
    
    def mouse_is_over(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + self.width and pos[1] >= self.y and pos[1] <= self.y + self.height:
            return True
        return False