from turtle import width
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
        self.bg = game.bg
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.world_shift = 0
        self.current_x = 0
        
        self.setup_level(level_map)
        
        self.moving_right = False
        self.moving_left = False
        
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
        self.rect_x = player.rect.centerx
        self.rect = player.rect
        direction_x = player.direction.x
        

        if self.bg.rect.right > self.screen_rect.right :
            if direction_x > 0 and self.rect.right < self.screen_rect.right:
                if self.rect_x < self.settings.screen_width - (self.settings.screen_width / 2):
                    player.speed = 8
                    self.world_shift = -1
                else:
                    player.speed = 0
                    self.world_shift = -8
                print('1')
            elif direction_x < 0 and self.rect.left > 0:
                self.world_shift = -1
                player.speed = 8
                print('2')
            else :
                self.world_shift = -1
                player.speed = 0
                print('3)')
                
        else:
            player.speed = 8
            self.world_shift = 0

        
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True 
                    self.current_x = player.rect.right
                    
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
                    
    def vertical_movement_collisoin(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False 
    
    def update(self):
        #self.tiles.update(self.world_shift)
        self.bg.update(self.world_shift)
        self.player.update()
             
    def drawTiles(self):
        #level tiles
        self.tiles.draw(self.screen)
        self.scroll_x()
    def drawPlayer(self):
        #player
        self.horizontal_movement_collision()
        self.vertical_movement_collisoin()
        self.player.draw(self.screen)
