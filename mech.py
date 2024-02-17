# import numpy as np
# import random


# grid = np.zeros((9, 9))


# type1 = str("type1")
# type2 = str("type2")


# start_x = random.randint(0, 8)
# start_y = random.randint(0, 8)


# def is_filled(grid):
#     return not (grid == 0).any()


# def get_neighbors(x, y):
#     neighbors = [(nx, ny) for nx in range(x-1, x+2) for ny in range(y-1, y+2)
#                  if 0 <= nx < 9 and 0 <= ny < 9 and (nx != x or ny != y)]
#     return neighbors


# while not is_filled(grid):
    
#     obj_type = random.choice([type1, type2])

    
#     if grid[start_x, start_y] == 0:
#         grid[start_x, start_y] = obj_type

    
#     neighbors = get_neighbors(start_x, start_y)

    
#     start_x, start_y = random.choice(neighbors)

# print(grid)
import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((500, 500))


array = [[j for j in range(i, i + 5)] for i in range(0, 25, 5)]


square_size = 50


colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0), (0, 128, 128), (128, 0, 128), (192, 192, 192), (128, 128, 128), (153, 76, 0), (76, 153, 0), (0, 76, 153), (153, 0, 76), (76, 153, 0), (0, 76, 153), (76, 0, 153), (153, 76, 0), (76, 0, 153), (0, 153, 76), (153, 0, 76)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    
    for i in range(5):
        for j in range(5):
            pygame.draw.rect(screen, colors[array[i][j]], pygame.Rect((250 - square_size / 2) + j * square_size, (250 - square_size / 2) + i * square_size, square_size, square_size))
            font = pygame.font.Font(None, 24)
            text = font.render(str(array[i][j]), True, (0, 0, 0))
            screen.blit(text, ((250 - square_size / 2) + j * square_size + square_size / 2, (250 - square_size / 2) + i * square_size + square_size / 2))

    pygame.display.flip()
