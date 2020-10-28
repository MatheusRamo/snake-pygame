from random import randint
import pygame

pygame.init()
width, height = 800, 800

black = (0,0,0)
screen = pygame.display.set_mode((width,height))


# Board
def Board(n):
    for row in range(n):
        for column in range(n):
            pygame.draw.rect(screen, (255, 255, 0),((20*column,20*row), (20,20)), 1)

# Snake
snake = pygame.Rect((400,400),(20,20))

food = pygame.Rect((randint(0,39)*20,randint(0,39)*20 ),(20,20))

runing = True
while runing:
    screen.fill(black)
    Board(40)
    pygame.draw.rect(screen, (255,0,255),snake)

    pygame.draw.rect(screen, (255,255,255), food)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        snake.y -= 20
    if key[pygame.K_s]:
        snake.y += 20
    if key[pygame.K_d]:
        snake.x += 20
    if key[pygame.K_a]:
        snake.x -= 20