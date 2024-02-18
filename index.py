
import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

def new_func():
    pygame.mixer.music.stop()
    os.system("python lvl.py")
    pygame.mixer.music.play(100,0,0)



background = pygame.image.load("assets\image\static\mainmenubg.png")
play_button = pygame.image.load("assets\image\static\playbutton.png")
settings_button = pygame.image.load("assets\image\static\settingbutton.png")
exit_button = pygame.image.load("assets\image\static\exitbutton.png")


play_bg = pygame.image.load("assets\image\static\ctbg.png")
settings_bg = pygame.image.load("assets\image\static\ctbg.png")
exit_bg = pygame.image.load("assets\image\static\ctbg.png")

play_rect = play_button.get_rect()
play_rect.center = (960, 600)
exit_rect = exit_button.get_rect()
exit_rect.center = (960, 700)


while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if play_rect.collidepoint(mouse_x, mouse_y):
                new_func()
            
            if exit_rect.collidepoint(mouse_x, mouse_y):
                sys.exit()

    
    screen.blit(background, (0, 0))

    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    play_alpha = max(0, min(255, 255 - (mouse_x - play_rect.centerx)**2, - (mouse_y - play_rect.centery)**2))
    exit_alpha = max(0, min(255, 255 - (mouse_x - exit_rect.centerx)**2, - (mouse_y - exit_rect.centery)**2))

    
    play_bg_copy = play_bg.copy()
    play_bg_copy.set_alpha(play_alpha)
    exit_bg_copy = exit_bg.copy()
    exit_bg_copy.set_alpha(exit_alpha)

    
    screen.blit(play_bg_copy, play_rect)
    screen.blit(exit_bg_copy, exit_rect)

    
    screen.blit(play_button, play_rect)
    screen.blit(exit_button, exit_rect)

    pygame.display.flip()