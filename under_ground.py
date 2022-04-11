import pygame as pg

class UnderGround:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.underground_finished = False
        self.underground = self.game.underground
        self.underground_rect = self.underground.get_rect()
        
    def draw(self):
        self.screen.blit(self.underground, self.underground_rect)
        
    def show(self):
        while not self.underground_finished:
            self.draw()
    