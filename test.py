
# import numpy as np

# array = np.zeros((5, 5), dtype=int)


# pos1 = np.random.choice(5, 2, replace=False)
# pos2 = np.random.choice(5, 2, replace=False)
# while np.array_equal(pos1, pos2):
#     pos2 = np.random.choice(5, 2, replace=False)
# array[pos1[0], pos1[1]] = 1
# array[pos2[0], pos2[1]] = 1
# print (array)


# x1, y1 = pos1
# x2, y2 = pos2
# while x1 != x2 or y1 != y2:
#     if x1 < x2:
#         x1 += 1
#     elif x1 > x2:
#         x1 -= 1
#     elif y1 < y2:
#         y1 += 1
#     elif y1 > y2:
#         y1 -= 1
#     array[x1, y1] = 1


# print(array)

import pygame
import sys
import os


pygame.init()

LVL_MUSIC = pygame.mixer.music.load("./assets/ost/Main_theme.wav")
pygame.mixer.music.play(100,0,0)

class calling:
    
    def init(self, files):
        
        self.files = files
        
        self.states = {}
       
        for file in self.files:
            self.states[file] = False

    
    def run(self, file):
        
        if file in self.files:
            
            if not self.states[file]:
                
                exec(open(file).read())
                
                self.states[file] = True
            else:
                
                print(f"{file} is already running.")
        else:
            
            print(f"{file} is not in the list of files.")

    
    def close(self, file):
        
        if file in self.files:
            
            if self.states[file]:
                
                pygame.quit()
                
                self.states[file] = False
            else:
                
                print(f"{file} is not running.")
        else:
            
            print(f"{file} is not in the list of files.")

    
    def check(self):
        
        running_files = []
        
        for file in self.files:
            
            if self.states[file]:
                running_files.append(file)
        
        return running_files
pygame.init()

screen = pygame.display.set_mode((1920, 1080))

def new_func():
    pygame.mixer.music.stop()
    os.system("py index.py")
    pygame.mixer.music.play(100,0,0)



background = pygame.image.load("assets\image\static\mainmenubg.png")
play_button = pygame.image.load("assets\image\static\playbutton.png")
settings_button = pygame.image.load("assets\image\static\settingbutton.png")
exit_button = pygame.image.load("assets\image\static\exitbutton.png")


play_bg = pygame.image.load("assets\image\static\ctbg.png")
settings_bg = pygame.image.load("assets\image\static\ctbg.png")
exit_bg = pygame.image.load("assets\image\static\ctbg.png")

play_rect = play_button.get_rect()
play_rect.center = (400, 200)
settings_rect = settings_button.get_rect()
settings_rect.center = (400, 300)
exit_rect = exit_button.get_rect()
exit_rect.center = (400, 400)


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