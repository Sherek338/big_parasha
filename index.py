import pygame
import random
import Events
import entity.Hero as Hero
import entity.Enemy as Enemy
import others.Cell as Cell
import others.Close as Close
import others.Button as Button


WIDTH, HEIGHT = 1920, 1080
ROWS, COLS = 8, 9
BLOCK_SIZE = 86
CENTER_MARGIN_X = (WIDTH / 2) - ((COLS * BLOCK_SIZE) / 2)
CENTER_MARGIN_Y = HEIGHT - 150 - (ROWS * BLOCK_SIZE)

pygame.init()
pygame.font.init()
pygame.display.init()

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# LVL_MUSIC = pygame.mixer.music.load("./assets/ost/lvl_theme.wav")
# pygame.mixer.music.play(100, 0, 0)

MAIN_BG = pygame.transform.scale(pygame.image.load("./assets/sprites/main_bg.png").convert(), (1550, 900))
ATTACK_BTN = pygame.image.load("./assets/sprites/attack_btn.png").convert_alpha()
font_attack = pygame.font.Font("./assets/fonts/Inter-Regular.ttf", 32)
font_lvl = pygame.font.Font("./assets/fonts/Inter-Bold.ttf",38) 

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

all_sprites = pygame.sprite.Group()

def draw_grid(grid, pos):
    posx, posy = pos
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if i == posy and j == posx:
                hero = Hero.HeroClass((j * BLOCK_SIZE + CENTER_MARGIN_X, i * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
                all_sprites.add(hero)
                grid[i][j] = Cell.CellClass(hero, (j, i))
                continue
            enemy = Enemy.EnemyClass(random.randint(1, 4), (j * BLOCK_SIZE + CENTER_MARGIN_X, i * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
            all_sprites.add(enemy)
            grid[i][j] = Cell.CellClass(enemy, (j, i))

def on_attack(props):
    cur_sequence = props[0]
    for cell in cur_sequence:
        all_sprites.remove(cell.item)

def main():
    clock = pygame.time.Clock()
    
    cur_type = -1
    cur_position = (4, 5)
    draw_grid(grid, cur_position)
    cur_sequence = [grid[5][4]]
    cur_sequence_set = set(cur_sequence)

    attack_btn = Button.ButtonClass((1350, 800), ATTACK_BTN, on_attack, font_attack.render("АТАКОВАТЬ", 1, (255, 255, 255)))
    lvl_label = font_lvl.render("УРОВЕНЬ 1", 1, (0, 0, 0))
    
    all_sprites.add(attack_btn)
    
    close_cells = Close.get_close(grid, cur_position, ROWS, COLS)
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                attack_btn.is_press(mx, my, [cur_sequence_set])
                for cell in close_cells:
                    if not cell.is_mouse_over(mx, my): 
                        continue
                    if cell in cur_sequence_set:
                        #TODO:path back
                        # if cur_sequence.index(cell) == len(cur_sequence) - 2:
                        #     last_cell = cur_sequence[len(cur_sequence) - 1]
                        #     cur_sequence_set.remove(cell)
                        #     cur_sequence.remove(cell)
                        #     cur_sequence[len(cur_sequence) - 1].set_default()
                        #     cur_position = last_cell.pos
                        #     cur_type = last_cell.item.type
                            continue
                    if cell not in cur_sequence_set and (cur_type == cell.item.type or cur_type == -1): 
                        cell.item.image.fill((0,0,0))
                        cur_type = cell.item.type
                        cur_position = cell.pos
                        cur_sequence.append(cell)
                        cur_sequence_set.add(cell)
                        close_cells = Close.get_close(grid, cur_position, ROWS, COLS)
            if event.type == Events.DEADTH_EVENT:
                #TODO:end game
                pass
            
        win.blit(MAIN_BG, (190, 100))
        win.blit(lvl_label, ((WIDTH / 2) - (lvl_label.get_rect().width / 2), 130))
        all_sprites.draw(win)
        
        for cell in close_cells:
            if cell in cur_sequence_set:
                cell.item.image.fill((0,0,0))
        
        all_sprites.update()
        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()