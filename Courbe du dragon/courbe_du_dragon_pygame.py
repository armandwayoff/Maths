import pygame
import numpy as np

WHITE = (255, 255, 255)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = SCREEN_HEIGHT

mat_rot_d = np.array([[0, 1], [-1, 0]])  # matrice de rotation vers la droite
mat_rot_g = -mat_rot_d  # matrice de rotation vers la gauche

T = np.array([400, 200])  # vecteur translation pour centrer la figure
M = np.array([0, 1])  # vecteur initial

DIM, L = 15, 1.8
courbe = [1]
rotations = []  # liste des vecteurs qui composeront l'ensemble du tracé

for k in range(DIM):
    courbe += [1] + [int(not e) for e in courbe][::-1]

for dir in courbe:
    if dir == 1:
        M = np.dot(mat_rot_d, M)
    else:
        M = np.dot(mat_rot_g, M)
    rotations.append(M)

launched = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Courbe du dragon d'ordre " + str(DIM))

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    screen.fill(WHITE)
    M0 = np.array([0, 1])
    for i in range(len(courbe) - 1):
        M1 = M0 + rotations[i]
        pygame.draw.line(screen, (0, 0, 0), L * M0 + T, L * M1 + T, 1)
        M0 = M1.copy()
    pygame.display.update()
