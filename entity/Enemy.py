import pygame
import random

class EnemyClass(pygame.sprite.Sprite):
    def __init__(self, type, pos, size):
        super().__init__()
        self.type = type
        self.psevdo = 5
        self.is_angry = False
        
        self.image = pygame.Surface(size) # None
        
        self.COLOR = None
        #TODO:sprites
        if self.type == 1:
            self.COLOR = (255, 0, 0)
        if self.type == 2:
            self.COLOR = (0, 125, 0)
        if self.type == 3:
            self.COLOR = (0, 0, 125)
        if self.type == 4:
            self.COLOR = (255, 255, 255)
        
        self.image.fill(self.COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
    def update(self):
        self.image = self.image
        if random.randint(0, 100) < self.psevdo:
            self.psevdo = 0
            self.is_angry = True
            return
        self.psevdo += 3
        