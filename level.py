import pygame as pg
from game_data import levels

class Level:
    def __init__(self, game, current_level):
        self.game = game
        self.settings = self.game.settings
       
        
        #level setup
        self.screen = game.screen
        self.current_level = current_level
        level_data = levels[self.current_level]
        level_content = level_data['content']
        self.new_max_level = level_data['unlock']
        self.create_overworld = self.game.create_overworld
        
        # level display
        self.font = pg.font.Font(None, 40)
        self.text_surf = self.font.render(level_content, True, 'White')
        self.text_rect = self.text_surf.get_rect(center = (self.settings.screen_width /2, self.settings.screen_height /2))
        
    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            self.create_overworld(self.current_level, self.new_max_level)
        if keys[pg.K_ESCAPE]:
            self.create_overworld(self.current_level, 0)
        
    def run(self):
        self.input()
        self.screen.blit(self.text_surf, self.text_rect)