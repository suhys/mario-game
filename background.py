import pygame as pg

class Background():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.background = pg.image.load(f'img/level/1-0.png')
        self.background = pg.transform.scale(self.background,
                                  (int(self.settings.screen_width*self.settings.background_multiplier),
                                  int(self.settings.screen_height)))
        self.rect = self.background.get_rect()
        self.rect_width = self.rect.width
        self.rect_height = self.rect.height
        self.rect = self.rect.move((0,0))
        
        self.underground = pg.image.load(f'img/level/1-1.png')
        self.underground = pg.transform.scale(self.background,
                                  (int(self.settings.screen_width*self.settings.background_multiplier),
                                  int(self.settings.screen_height)))
        
    def update(self,x_shift):
        self.rect.x += x_shift
        