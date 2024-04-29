import pygame

WIDTH, HEIGHT = 800,800
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS

## rgb
RED = (217, 140, 89)
WHITE = (193, 227, 208)
BLACK = (0,0,0)
BLUE = (50, 105, 168)
GREEN = (62, 92, 23)
L_GREEN = (127, 168, 74)
GREY = (128,128,128)

COROA = pygame.transform.scale(pygame.image.load('source/assets/crown.png'), (45,25))