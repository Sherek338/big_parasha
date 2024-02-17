import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, item, rect: pygame.Rect) -> None:
        super().__init__()
        self.item = item
        self.rect = rect
    
    def is_mouse_over(self, mx, my, cur_type):
        self.rect.collidepoint(mx, my)
        if self.item.type == cur_type:
            #TODO:Animation
            return True
        return False
        