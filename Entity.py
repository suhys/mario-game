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
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
=======
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
        self.direction = pg.math.Vector2(-1,0)


    def update(self,x_shift):
        self.rect.x += x_shift
        self.rect.x += self.direction.x
<<<<<<< HEAD
<<<<<<< HEAD

=======
=======
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
        
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
class Mushroom(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pg.image.load(f'img/Mushroom.png')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
<<<<<<< HEAD
<<<<<<< HEAD
        self.rect.x += x_shift 
        self.rect.x += x_shift
=======
        self.rect.x += x_shift
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
=======
        self.rect.x += x_shift
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
