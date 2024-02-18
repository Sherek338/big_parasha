import pygame
import Events as Events

class HeroClass(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.defend = False
        self.type = 0
        
        self.is_angry = False
        self.image = pygame.transform.scale(pygame.image.load("./assets/image/animated/dynamic/hero/hero_!.png"), (120, 120))
        self.image_selected = self.image
        self.rect = self.image.get_rect() 
        self.x, self.y = pos
        self.rect.topleft = (self.x - 20, self.y -20)
        
    def get_damage(self, damage):
        if self.defend:
            return
        self.hp -= damage
        if self.hp < 0:
            self.death()
            
    def death(self):
        pygame.event.post(pygame.event.Event(Events.DEADTH_EVENT))
        
    def update(self):
        pass