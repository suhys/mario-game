from tracemalloc import start
from turtle import end_fill
import pygame as pg
from game_data import levels
from pygame.sprite import Group, Sprite, GroupSingle

class Overworld:
    def __init__(self, game):
        #setup
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.max_level = self.settings.max_level
        self.start_level = self.settings.start_level
        self.current_level = self.settings.start_level
        
        # movement logic
        self.moving = False
        self.move_direction = pg.math.Vector2(0,0)
        self.speed = 8.0
    
        #sprites
        self.nodes = Group()
        self.setup_nodes()
        self.setup_icon()
        
    def setup_nodes(self):
        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available', self.speed)
            else:
                node_sprite = Node(node_data['node_pos'], 'locked', self.speed)
            self.nodes.add(node_sprite)
            
    def draw_paths(self):
        points = [node['node_pos'] for index,node in enumerate(levels.values()) if index <= self.max_level]
        pg.draw.lines(self.screen, 'red', False, points, 6)
        
    def setup_icon(self):
        self.icon = GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)
    
    def input(self):
        # move icon
        keys = pg.key.get_pressed()
        
        if not self.moving:
            if keys[pg.K_RIGHT]:
                if self.current_level != self.max_level:
                    self.move_direction = self.get_movement_data('next')
                    self.current_level += 1
                    self.moving = True
            elif keys[pg.K_LEFT]:
                if self.current_level > 0:
                    self.move_direction = self.get_movement_data('previous')
                    self.current_level -= 1
                    self.moving = True
                
    def get_movement_data(self, target):
        start = pg.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
        
        if target == 'next':
            end = pg.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pg.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

        return(end-start).normalize()
    
    def update_icon_pos(self):
        if self.moving and self.move_direction:
            # update icon position based on the input
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pg.math.Vector2(0,0)
            

    def run(self):
        self.input()
        self.update_icon_pos()
        self.icon.update()
        self.draw_paths()
        self.nodes.draw(self.screen)
        self.icon.draw(self.screen)
        
class Icon(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pos
        self.image = pg.Surface((20,20))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = self.pos)
        
    def update(self):
        self.rect.center = self.pos

class Node(Sprite):
    def __init__(self,pos,status,icon_speed):
        super().__init__()
        self.image = pg.Surface((100, 80))
        if status == 'available':
            self.image.fill('red')
        else:
            self.image.fill('gray')
        self.rect = self.image.get_rect(center = pos)
        
        self.detection_zone = pg.Rect(self.rect.centerx-(icon_speed/2),self.rect.centery-(icon_speed/2),icon_speed,icon_speed)