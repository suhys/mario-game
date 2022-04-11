import pygame as pg
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pg.image.load(f'img/Coin.png')
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self,x_shift):
        self.rect.x += x_shift
        
    def update(self,x_shift):
        self.rect.x += x_shift
        
class Gumba(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load(f'img/gumba.png'), 0,2)
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pg.math.Vector2(-1,0)


    def update(self,x_shift):
        self.rect.x += x_shift
        self.rect.x += self.direction.x
        
class Mushroom(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pg.image.load(f'img/Mushroom.png')
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self,x_shift):
        self.rect.x += x_shift