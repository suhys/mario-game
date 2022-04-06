import pygame as pg
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pg.image.load(f'img/Coin.png')
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self,x_shift):
        self.rect.x += x_shift