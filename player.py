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
        
        # player movement
        self.direction = pg.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        
    def input(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pg.K_SPACE]:
            self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.input()