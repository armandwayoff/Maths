import pygame
import random as rd

LENGTH = 100
INTEGERS = [k for k in range(10)]

X, Y = [rd.choice(INTEGERS) for _ in range(LENGTH)], [rd.choice(INTEGERS) for _ in range(LENGTH)]

WHITE = (255, 255, 255)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = SCREEN_HEIGHT
LENGTH_LINE = SCREEN_HEIGHT / LENGTH

launched = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    screen.fill(WHITE)
    for i in range(LENGTH):
        if X[i] % 2 == 0:
            for j in range(0, LENGTH - 1, 2):
                pygame.draw.line(screen, "black", (i * LENGTH_LINE, j * LENGTH_LINE), (i * LENGTH_LINE, (j + 1) * LENGTH_LINE))
        else:
            for j in range(1, LENGTH - 1, 2):
                pygame.draw.line(screen, "black", (i * LENGTH_LINE, j * LENGTH_LINE), (i * LENGTH_LINE, (j + 1) * LENGTH_LINE))
    for j in range(LENGTH):
        if Y[j] % 2 == 0:
            for i in range(0, LENGTH - 1, 2):
                pygame.draw.line(screen, "black", (i * LENGTH_LINE, j * LENGTH_LINE), ((i + 1) * LENGTH_LINE, j * LENGTH_LINE))
        else:
            for i in range(1, LENGTH - 1, 2):
                pygame.draw.line(screen, "black", (i * LENGTH_LINE, j * LENGTH_LINE), ((i + 1) * LENGTH_LINE, j * LENGTH_LINE))
    pygame.display.update()
