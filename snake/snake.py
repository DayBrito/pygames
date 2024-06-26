import pygame, random
from pygame.locals import *

## Função pra gridar o random da maçã
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//30*30, y//30*30)

def colisao (c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

posicao_maca = on_grid_random()
maca = pygame.Surface((10,10))
maca.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',18)
score = 0

game_over = False
while not game_over:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        ## DEFININDO EVENTOS DE TECLA PARA CONTROLAR
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = RIGHT
            if event.key == K_RIGHT:
                my_direction = LEFT
    
    if colisao(snake[0], posicao_maca):
        posicao_maca = on_grid_random()
        snake.append((0,0))
        score+=1
    
    if snake[0][0] == 600 or snake[0][1] == 600 or snake [0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    ## DEFINIDO POSIÇÃO DO CORPO DA cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] +10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] +10, snake[0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] -10, snake[0][1])


    screen.fill((0,0,0))
    screen.blit(maca, posicao_maca)

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for posicao in snake:
        screen.blit(snake_skin,posicao)
    

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 55)
    game_over_screen = game_over_font.render('game over :(', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(10)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

