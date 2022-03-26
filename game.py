import pygame as pg
import sys
from settings import Settings
from overworld import Overworld

class Game:
    
    def __init__(self):
        #initialize pygame, settings, and screen object
        pg.init()
        self.settings = Settings()
        
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        # self.clock = pygame.time.Clock()
        
        self.overworld = Overworld(game = self)
        
        pg.display.set_caption("Mario Game")
        
    def draw(self):
        self.screen.fill(self.bg_color)
        pg.display.flip()
        
    def run(self):
        self.overworld.run()
        
    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            self.run()
            self.draw()
            
            pg.display.update()
            # self.clock.tick(60)
        
def main():
    game = Game()
    game.run_game()
    
if __name__ == '__main__':
    main()