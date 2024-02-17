import pygame
import random


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
BLOCK_SIZE = WIDTH//COLS


COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]


grid = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, color in enumerate(row):
            pygame.draw.rect(win, color, (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass  
        
        draw_grid(win, grid)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()