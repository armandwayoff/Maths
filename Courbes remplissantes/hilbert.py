import pygame
import numpy as np


def new_board(matrix):
    def m(mat, index):
        m_index = mat.copy()
        if index == 1:
            return m_index[::-1, ::-1].T
        elif index == 2:
            m_index += 4 ** dim
            return m_index
        elif index == 3:
            m_index += 2 * 4 ** dim
            return m_index
        else:
            m_index += 3 * 4 ** dim
            return m_index.transpose()

    s_w = m(matrix, 1).copy()
    n_w = m(matrix, 2).copy()
    n_e = m(matrix, 3).copy()
    s_e = m(matrix, 4).copy()
    top = np.array([np.concatenate([n_w[i], n_e[i]]) for i in range(2 ** dim)])
    bottom = np.array([np.concatenate([s_w[i], s_e[i]]) for i in range(2 ** dim)])
    return np.concatenate([top, bottom])


def coords(k, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == k:
                return [j, i]


WHITE = (255, 255, 255)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = SCREEN_HEIGHT

FINAL_DIM = 5  # max 6

launched = True

dim = 1
board = np.array([[2, 3], [1, 4]])

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hilbert Curve (dimension " + str(FINAL_DIM) + ")")

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    while dim < FINAL_DIM:
        board = new_board(board)
        dim += 1
        if dim == FINAL_DIM:
            screen.fill(WHITE)
            cell_width = SCREEN_HEIGHT / (2 ** dim)
            R, G, B = 255, 0, 0
            for k in range(1, 4 ** dim):
                x1, y1 = (coords(k, board)[0] + 1/2) * cell_width, (coords(k, board)[1] + 1/2) * cell_width
                x2, y2 = (coords(k + 1, board)[0] + 1/2) * cell_width, (coords(k + 1, board)[1] + 1/2) * cell_width
                pygame.draw.line(screen, (R, G, B), [x1, y1], [x2, y2], 3)
                R -= 255 / 4 ** dim
                G += 255 / 4 ** dim
    pygame.display.update()
    
