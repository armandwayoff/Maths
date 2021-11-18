from math import floor, sqrt
import pygame


def spiral(spiral_size, central_number):
    matrix = [[[] for col in range(spiral_size)] for row in range(spiral_size)]  # create an empty matrix
    x = y = floor(spiral_size / 2)
    for n in range(central_number, spiral_size ** 2 + central_number):
        matrix[y][x] = n
        move = floor((sqrt(4 * (n - central_number) + 1) + 3) % 4 + 1)  # for more information see
        # https://oeis.org/A063826
        if move == 1:
            x += 1  # move to the right
        elif move == 2:
            y -= 1  # move up
        elif move == 3:
            x -= 1  # move to the left
        else:
            y += 1  # move down
    return matrix


def moves(matrix, coords):
    x, y = coords[0], coords[1]
    targets = [
        matrix[x + 2][y + 1],
        matrix[x + 2][y - 1],
        matrix[x - 2][y + 1],
        matrix[x - 2][y - 1],
        matrix[x + 1][y + 2],
        matrix[x + 1][y - 2],
        matrix[x - 1][y + 2],
        matrix[x - 1][y - 2],
    ]
    return min([t for t in targets if t > 0])


def delete(matrix, val):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == val:
                matrix[i][j] = 0
                return i, j


WHITE = (255, 255, 255)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = SCREEN_HEIGHT

spiral_size, central_number = 71, 1  # the size of the spiral must be an odd number

STEP = 2015  # max 2016
A316667 = [1]
mat = spiral(spiral_size, central_number)
mat_ref = spiral(spiral_size, central_number)
coords = delete(mat, 1)
COORDS = [coords]

for i in range(STEP):
    next_step = moves(mat, coords)
    A316667.append(next_step)
    coords_next_step = delete(mat, next_step)
    coords = coords_next_step
    COORDS.append(coords)

launched = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    screen.fill(WHITE)
    cell_width = SCREEN_HEIGHT / spiral_size
    for k in range(len(A316667) - 1):
        x1, y1 = (COORDS[k][1] + 1 / 2) * cell_width, (COORDS[k][0] + 1 / 2) * cell_width
        x2, y2 = (COORDS[k + 1][1] + 1 / 2) * cell_width, (COORDS[k + 1][0] + 1 / 2) * cell_width
        pygame.draw.line(screen, (0, 0, 0), [x1, y1], [x2, y2], 1)

    pygame.display.update()
