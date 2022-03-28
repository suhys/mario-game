import pygame as pg
from game_data import levels, level_map
from pygame.sprite import Group
from tile import Tile

class OverWorldLevel:
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
        

class GameLevel:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.setup_level(level_map)
        
    def setup_level(self, layout):
        self.tiles = Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * self.settings.tile_size
                    y = row_index * self.settings.tile_size
                    tile = Tile((x,y),self.settings.tile_size)
                    print('add')
                    self.tiles.add(tile)
                    
            
        
    def draw(self):
        self.tiles.update(self.settings.world_shift)
        self.tiles.draw(self.screen)