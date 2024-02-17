import pygame

class EnemyClass(pygame.sprite.Sprite):
    def __init__(self, type, pos, size):
        super().__init__()
        self.type = type
        
        self.image = pygame.Surface(size) # None
        
        #TODO:sprites
        if self.type == 1:
            self.image.fill((255, 0, 0))
        if self.type == 2:
            self.image.fill((0, 125, 0))
        if self.type == 3:
            self.image.fill((0, 0, 125))
        if self.type == 4:
            self.image.fill((255, 255, 255))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
    def update(self):
        pass