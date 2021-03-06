import pygame as pg
from pygame.sprite import Sprite

class Tile(Sprite):
    def __init__(self,pos,width, height,color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self,x_shift):
        self.rect.x += x_shift