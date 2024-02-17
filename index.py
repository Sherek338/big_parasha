import pygame
import random
import Events
import entity.Hero as Hero
import entity.Enemy as Enemy
import others.Cell as Cell
import others.Close as Close


WIDTH, HEIGHT = 1920, 1080
ROWS, COLS = 8, 9
BLOCK_SIZE = 750//COLS
CENTER_MARGIN_X = (WIDTH / 2) - ((COLS * BLOCK_SIZE) / 2)
CENTER_MARGIN_Y = HEIGHT - 150 - (ROWS * BLOCK_SIZE)


COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

all_sprites = pygame.sprite.Group()

def draw_grid(grid, posx, posy):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if i == posy and j == posx:
                hero = Hero.HeroClass((j * BLOCK_SIZE + CENTER_MARGIN_X, i * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
                all_sprites.add(hero)
                grid[i][j] = Cell.CellClass(hero)
                continue
            enemy = Enemy.EnemyClass(random.randint(1, 4), (j * BLOCK_SIZE + CENTER_MARGIN_X, i * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
            all_sprites.add(enemy)
            grid[i][j] = Cell.CellClass(enemy)

def main():
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    
    draw_grid(grid, 4, 5)
    # list = Close.get_close(grid, 8, 0, ROWS, COLS)
    
    # for item in list:
    #     item.update()
    
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass  
            if event.type == Events.DEADTH_EVENT:
                #TODO:end game
                pass
        win.blit(pygame.image.load("./assets/123.jpg"), (0, 0))
        
        all_sprites.draw(win)
        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()