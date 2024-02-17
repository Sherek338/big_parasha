import pygame
import Events as Events

class HeroClass(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.defend = False
        self.type = 0
        
        self.is_angry = False
        self.COLOR = (125, 0, 0)
        self.image = pygame.Surface(size) #TODO:sprites
        self.image_selected = self.image
        self.image.fill(self.COLOR)
        self.rect = self.image.get_rect() 
        self.rect.topleft = pos
        
    def get_damage(self, damage):
        if self.defend:
            return
        self.hp -= damage
        if self.hp < 0:
            self.death()
            
    def death(self):
        #TODO:animation death
        pygame.event.post(pygame.event.Event(Events.DEADTH_EVENT))
        
    def update(self):
        pass