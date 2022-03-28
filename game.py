import pygame as pg
import sys
from settings import Settings
from overworld import Overworld
from level import Level

class Game:
    
    def __init__(self):
        #initialize pygame, settings, and screen object
        pg.init()
        self.settings = Settings()
        
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.clock = pg.time.Clock()
        
        self.overworld = Overworld(game = self, current_level=0)
        self.status = 'overworld'
        
        pg.display.set_caption("Mario Game")
        
    def create_level(self, current_level):
        self.level = Level(game=self, current_level = current_level)
        self.status = 'level'
        
    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.settings.max_level:
            self.settings.max_level = new_max_level
        self.overworld = Overworld(game=self, current_level=current_level )
        self.status = 'overworld'
        
    def draw(self):
        self.screen.fill(self.bg_color)
        
    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
        
    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            self.draw() 
            self.run()
            
            pg.display.update()
            self.clock.tick(60)
        
def main():
    game = Game()
    game.run_game()
    
if __name__ == '__main__':
    main()