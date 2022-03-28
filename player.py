import pygame as pg
from pygame.sprite import Group, Sprite
from settings import Settings

class Player(Sprite):
    player_image = pg.transform.rotozoom(pg.image.load(f'img/Mario.png'),0,2)
    
    def __init__(self, pos):
        super().__init__()
        self.image = Player.player_image
        self.settings = Settings()
        self.rect = self.image.get_rect(bottomleft = pos)
        self.direction = pg.math.Vector2(0,0)
        self.speed = 8
        
    def input(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed