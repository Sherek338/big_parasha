import pygame

class CellClass(pygame.sprite.Sprite):
    def __init__(self, item, pos) -> None:
        super().__init__()
        self.item = item
        self.rect = item.rect
        self.pos = pos
    
    def is_mouse_over(self, mx, my):
        if self.rect.collidepoint(mx, my):
                #TODO:Animation
                return True
        return False
    
    def set_default(self):
        self.item.image = self.item.image_reg