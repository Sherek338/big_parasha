import pygame

class CellClass(pygame.sprite.Sprite):
    def __init__(self, item) -> None:
        super().__init__()
        self.item = item
        self.rect = item.rect
    
    def is_mouse_over(self, mx, my, cur_type):
        self.rect.collidepoint(mx, my)
        if self.item.type == cur_type:
            #TODO:Animation
            return True
        return False
    
    def update(self):
        self.item.image.fill((0, 0, 0))
        