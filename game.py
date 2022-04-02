import pygame as pg
import sys
from background import Background
from settings import Settings
from overworld import Overworld
from level import *
from tile import Tile
from background import Background
from landing_page import LandingPage
from sound import Sound
from game_stats import GameStats
from scoreboard import Scoreboard
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
        self.tile = Tile
        self.stats = GameStats(game=self)
        self.scoreboard = Scoreboard(game=self)
        self.sound = Sound()
        
        self.clock = pg.time.Clock()
        
        # self.overworld = Overworld(game = self, current_level=0)
        self.gamelevel = GameLevel(game=self)
        
        # self.status = 'overworld'
        
        pg.display.set_caption("Mario Game")

    #overworld - but not going to use for this project
    # def create_level(self, current_level):
    #     # self.over_world_level = OverWorldLevel(game=self, current_level = current_level)
    #     self.status = 'level'
        
    # def create_overworld(self, current_level, new_max_level):
    #     if new_max_level > self.settings.max_level:
    #         self.settings.max_level = new_max_level
    #     self.overworld = Overworld(game=self, current_level=current_level )
    #     self.status = 'overworld' 
        
    def update(self):
        self.gamelevel.update()
        self.scoreboard.update()
        
    def draw(self): 
        self.screen.fill(self.bg_color)
        # self.gamelevel.tiles.draw(self.screen)
        self.screen.blit(self.background, self.bg.rect)
        self.gamelevel.draw()
        self.scoreboard.draw()
                
    def run(self):
        self.update()
        self.draw()
        
    def run_game(self):
        self.sound.play_bg()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
        
            self.run()
            
            pg.display.update()
            self.clock.tick(60)
    
    def game_over(self): 
        print('\nGAME OVER!\n\n')
        self.sound.play_game_over()
        main()
        
        
def main():
    game = Game()
    lp = LandingPage(game=game)
    lp.show()
    game.run_game()
    
if __name__ == '__main__':
    main()