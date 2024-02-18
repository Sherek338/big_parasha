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

LVL_MUSIC = pygame.mixer.music.load("./assets/ost/lvl_theme.wav")
pygame.mixer.music.play(100, 0, 0)

MAIN_BG = pygame.transform.scale(pygame.image.load("./assets/sprites/main_bg.png").convert(), (1550, 900))
ATTACK_BTN = pygame.image.load("./assets/sprites/attack_btn.png").convert_alpha()
ORNAMENT = pygame.image.load("./assets/sprites/orn.png").convert_alpha()
HEART_FULL = pygame.image.load("./assets/sprites/HP_FULL.png").convert_alpha()
HEART_LOST = pygame.image.load("./assets/sprites/HP_LOST.png").convert_alpha()
GAME_NAME = pygame.image.load("./assets/sprites/NAME.png").convert_alpha()

font_attack = pygame.font.Font("./assets/fonts/Inter-Regular.ttf", 32)

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
            enemy = Enemy.EnemyClass(random.randint(1, 3), (j * BLOCK_SIZE + CENTER_MARGIN_X, i * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
            all_sprites.add(enemy)
            grid[i][j] = Cell.CellClass(enemy, (j, i))

def on_attack(props):
    cur_sequence = props[0]
    if len(cur_sequence) < 2:
        return
    hero_cell = cur_sequence[len(cur_sequence) - 1:][0]
    herx, hery = hero_cell.pos
    hero = Hero.HeroClass((herx * BLOCK_SIZE + CENTER_MARGIN_X, hery * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
    all_sprites.remove(hero_cell.item)
    all_sprites.add(hero)
    grid[hery][herx] = Cell.CellClass(hero, (herx, hery))
    for cell in cur_sequence[0:len(cur_sequence) - 1]:
        all_sprites.remove(cell.item)
        x, y = cell.pos
        enemy = Enemy.EnemyClass(random.randint(1, 3), (x * BLOCK_SIZE + CENTER_MARGIN_X, y * BLOCK_SIZE + CENTER_MARGIN_Y), (BLOCK_SIZE, BLOCK_SIZE))
        grid[y][x] = Cell.CellClass(enemy, (x, y))
        all_sprites.add(enemy)

def main():
    clock = pygame.time.Clock()
    
    hp = 3
    
    cur_type = -1
    cur_position = (4, 5)
    
    draw_grid(grid, cur_position)
    
    cur_sequence = [grid[5][4]]
    cur_sequence_set = set(cur_sequence)
    
    heart_pos = [(250, 720), (250, 500), (250, 270)]    

    attack_btn = Button.ButtonClass((1350, 800), ATTACK_BTN, on_attack, font_attack.render("АТАКОВАТЬ", 1, (255, 255, 255)))
    
    all_sprites.add(attack_btn)
    
    btnGroup = pygame.sprite.Group()
    
    can_play = True
    game_over_rect = pygame.Surface((500, 300))
    game_over_rect.fill((249,224,193))
    game_over_label = font_attack.render("Game Over", 1, (0,0,0))
    main_menu_btn_rect = pygame.Surface((300, 100))
    main_menu_btn_rect.fill((250,238,203))
    main_menu_btn =  Button.ButtonClass((810, 550), main_menu_btn_rect, lambda props : None, font_attack.render("Главное меню", 1, (0,0,0)))
    btnGroup.add(main_menu_btn)
    
    close_cells = Close.get_close(grid, cur_position, ROWS, COLS)
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                main_menu_btn.is_press(mx, my, [])
                if can_play:
                    if attack_btn.is_press(mx, my, [cur_sequence]):
                        cur_type = -1
                        x, y = cur_position
                        cur_sequence = [grid[y][x]]
                        cur_sequence_set = set(cur_sequence)
                        for cell in close_cells:
                            if cell.item.is_angry:
                                hp -= 1
                                if hp <= 0:
                                    pygame.event.post(pygame.event.Event(Events.DEADTH_EVENT)) 
                    for cell in close_cells:
                        if not cell.is_mouse_over(mx, my): 
                            continue
                        if cell in cur_sequence_set:
                            continue
                        if cur_type == cell.item.type or cur_type == -1: 
                            cell.item.image = cell.item.image_selected
                            cur_type = cell.item.type
                            cur_position = cell.pos
                            cur_sequence.append(cell)
                            cur_sequence_set.add(cell)
                            close_cells = Close.get_close(grid, cur_position, ROWS, COLS)
            if event.type == Events.DEADTH_EVENT:
                cur_sequence[0].item.image = pygame.image.load()
                can_play = False
            
        win.blit(MAIN_BG, (190, 100))
        win.blit(GAME_NAME, ((WIDTH / 2) - (GAME_NAME.get_rect().width / 2), 130))
        win.blit(ORNAMENT, (1420, 150))
        
        count = 0
        for pos in heart_pos:
            if count < hp:
                count += 1
                win.blit(HEART_FULL, pos)
            else:
                win.blit(HEART_LOST, pos)
        
        all_sprites.draw(win)
        
        for cell in close_cells:
            if cell in cur_sequence_set:
                cell.item.image = cell.item.image_selected
        
        all_sprites.update()
        
        if not can_play:
            win.blit(game_over_rect, (710, 450))
            win.blit(game_over_label, (870, 470))
            btnGroup.draw(win)
        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()