from tkinter import UNDERLINE
from turtle import width
import pygame as pg
from game_data import UnderGround_map, level_map
from player import Player
from pygame.sprite import Group
from tile import Tile
from Entity import Coin, Gumba


class GameLevel:
    def __init__(self, game):
        self.game = game
        self.bg = game.bg
        self.stats = game.stats
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.world_shift = 0
        self.current_x = 0
        
        self.setup_level(level_map)
        
        self.moving_right = False
        self.moving_left = False
        self.coin_points = 20
        
        self.underground = False
        
    def setup_level(self, layout):
        self.tiles = Group()
        self.player = pg.sprite.GroupSingle()
        self.enter = Group()
        self.question = Group()
        self.coin = Group()
        self.invisible = Group()
        self.g = Group()
        self.fall= Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * self.settings.tile_width
                y = row_index * self.settings.tile_height
                if cell == 'X' or cell == 'P' or cell == '?':
                    tile = Tile((x,y),self.settings.tile_width, self.settings.tile_height,'Gray')
                    self.tiles.add(tile)
                if cell == 'A':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'E':
                    Enter = Tile((x,y),self.settings.tile_width, self.settings.tile_height,'Green')
                    self.enter.add(Enter)
                if cell == '?':
                    question = Tile((x,y),self.settings.tile_width, self.settings.tile_height,'Brown')
                    self.question.add(question)
                if cell == 'C':
                    coin = Coin((x,y))
                    self.coin.add(coin)
                if cell == 'I':
                    invisible = Tile((x,y),self.settings.tile_width, self.settings.tile_height,'Blue')
                    self.invisible.add(invisible)
                if cell == 'F':
                    fall = Tile((x,y),self.settings.tile_width, self.settings.tile_height,'Pink')
                    self.fall.add(fall)
                if cell == 'G':
                    g = Gumba((x,y))
                    self.g.add(g)
<<<<<<< HEAD
<<<<<<< HEAD
                if cell == 'F':
                    fall = Tile((x,y),self.settings.tile_width, self.settings.tile_height,'Pink')
                    self.fall.add(fall)
=======

                
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
=======

                
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
                    
    def collision(self):
        player = self.player.sprite
        self.rect_x = player.rect.centerx
<<<<<<< HEAD
<<<<<<< HEAD
        self.rect_bottom = player.rect.bottom
=======
        self.rect = player.rect
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
=======
        self.rect = player.rect
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
        collisions = pg.sprite.groupcollide(self.coin, self.player, True, False)
        for coin in collisions:
             self.stats.coin_score += self.coin_points
             self.stats.score_update()
<<<<<<< HEAD
<<<<<<< HEAD
        print (self.coin_points)
        if pg.sprite.groupcollide(self.g, self.player, False,False):
            for gumba in self.g:
                if gumba.rect.top == self.rect_bottom:
                    gumba.kill()
                    print("kill")
                else:
                    self.game.status = 'gameover'   
        # if pg.sprite.groupcollide(self.g, self.player, True,True):
        #     self.game.status = 'gameover'   
=======
        if pg.sprite.groupcollide(self.g, self.player, True,True): 
            self.game.status = 'gameover'   
        pg.sprite.groupcollide(self.question, self.player, True,False)
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
=======
        if pg.sprite.groupcollide(self.g, self.player, True,True): 
            self.game.status = 'gameover'   
        pg.sprite.groupcollide(self.question, self.player, True,False)
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
        for gumba in self.g:
            if pg.sprite.spritecollide(gumba, self.tiles, False): 
                if gumba.direction.x==1:
                    gumba.direction.x=-1
                else:
                    gumba.direction.x=1
            pg.sprite.spritecollide(gumba, self.fall, True)
<<<<<<< HEAD
<<<<<<< HEAD
        
        # if pg.sprite.groupcollide(self.enter, self.player, False, False):
        #     if player.down:
        #         self.underground = True
        #         print("underground")
=======
=======
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
        # for gumba in self.g:
        #     if pg.Rect.collidepoint(self.player, gumba.rect.top):
        #         gumba.kill
        #     if pg.Rect.collidepoint(self.player, gumba.rect.top) == False:
        #         self.game.status = 'gameover'
>>>>>>> 7386a61f962c6c571161628492edcec10a18bf8f
    
    def scroll_x(self):
        player = self.player.sprite
        self.rect_x = player.rect.centerx
        self.rect = player.rect
        direction_x = player.direction.x
        
        if self.bg.rect.right > self.screen_rect.right :
            if direction_x > 0 and self.rect.right < self.screen_rect.right:
                if self.rect_x < self.settings.screen_width - (self.settings.screen_width / 2):
                    player.speed = 8
                    self.world_shift = 0
                else:
                    player.speed = 0
                    self.world_shift = -8
            elif direction_x < 0 and self.rect.left > 0:
                self.world_shift = 0
                player.speed = 8
            else :
                self.world_shift = 0
                player.speed = 0
                
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
            
    def falling(self):
        player = self.player.sprite
        self.rect = player.rect
        if player.rect.bottom > self.screen_rect.bottom:
            self.game.status = 'gameover'
    
    def update(self):
        self.tiles.update(self.world_shift)
        self.question.update(self.world_shift)
        self.enter.update(self.world_shift)
        self.coin.update(self.world_shift)
        self.invisible.update(self.world_shift)
        self.g.update(self.world_shift)
        self.bg.update(self.world_shift)
        self.player.update()
        self.scroll_x()
        self.horizontal_movement_collision()
        self.vertical_movement_collisoin()
        self.falling()
        self.collision()
             
    def draw(self):
        # level tiles
        # self.tiles.draw(self.screen)
        # self.question.draw(self.screen)
        # self.pipe.draw(self.screen)
        self.coin.draw(self.screen)
        self.invisible.draw(self.screen)
        self.g.draw(self.screen)
        #player
        self.player.draw(self.screen)
