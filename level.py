import pygame as pg
from game_data import levels, level_map
from player import Player
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
        
        self.world_shift = 0
        
        self.setup_level(level_map)
        
    def setup_level(self, layout):
        self.tiles = Group()
        self.player = pg.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * self.settings.tile_size
                y = row_index * self.settings.tile_size
                if cell == 'X':
                    tile = Tile((x,y),self.settings.tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < self.settings.screen_width / 2 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > self.settings.screen_width - (self.settings.screen_width / 2) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
        
    
    def update(self):
        self.tiles.update(self.world_shift)
        self.player.update()
             
    def draw(self):
        #level tiles
        self.tiles.draw(self.screen)
        #player
        self.player.draw(self.screen)
        self.scroll_x()