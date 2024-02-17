import pygame
import Events as Events

class Hero:
    def __init__(self):
        super().__init__()
        self.hp = 3
        self.defend = False
        
    def get_damage(self, damage):
        if self.defend:
            return
        self.hp -= damage
        if self.hp < 0:
            self.death()
            
    def death(self):
        #TODO:animation death
        pygame.event.post(Events.DEADTH_EVENT)