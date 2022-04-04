import pygame as pg
import sys
from background import Background
from settings import Settings
from overworld import Overworld
from level import *
from tile import Tile
from background import Background

class Game:
    
    def __init__(self):
        #initialize pygame, settings, and screen object
        pg.init()
        self.settings = Settings()
        
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.bg = Background(game = self)
        self.background = self.bg.background
        
        self.clock = pg.time.Clock()
        
        self.overworld = Overworld(game = self, current_level=0)
        self.gamelevel = GameLevel(game=self)
        
        self.status = 'overworld'
        
        pg.display.set_caption("Mario Game")
        
    def create_level(self, current_level):
        self.OverWorldLevel = OverWorldLevel(game=self, current_level = current_level)
        self.status = 'level'
        
    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.settings.max_level:
            self.settings.max_level = new_max_level
        self.overworld = Overworld(game=self, current_level=current_level )
        self.status = 'overworld'
        
    def update(self):
        self.gamelevel.update()
        
    def draw(self): 
        self.screen.fill(self.bg_color)
        self.gamelevel.drawTiles()
        self.screen.blit(self.background, self.bg.rect)
        self.gamelevel.drawPlayer()
                
    def run(self):
        # if self.status == 'overworld':
        #     self.overworld.run()
        # else:
        #     self.level.run()
        pass
        
    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
        
            
            self.update()
            self.draw() 
            # self.run()
            
            pg.display.update()
            self.clock.tick(60)
        
def main():
    game = Game()
    game.run_game()
    
if __name__ == '__main__':
    main()
