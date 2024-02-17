import pygame

class ButtonClass(pygame.sprite.Sprite):
    def __init__(self, pos, background, onclick, label = None) -> None:
        super().__init__()
        self.onclick = onclick
        
        self.image = background
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
        if label is not None:
            self.image.blit(label, (((self.rect.width / 2) - (label.get_rect().width / 2)), ((self.rect.height / 2) - (label.get_rect().height / 2))))
    
    def is_press(self, mx, my, props):
        if self.rect.collidepoint(mx, my):
            self.onclick(props)
            return True
        return False