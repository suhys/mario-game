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
        self.current_level = self.settings.start_level
    
        #sprites
        self.nodes = Group()
        self.setup_nodes()
        self.setup_icon()
        
    def setup_nodes(self):
        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available')
            else:
                node_sprite = Node(node_data['node_pos'], 'locked')
            self.nodes.add(node_sprite)
            
    def draw_paths(self):
        points = [node['node_pos'] for index,node in enumerate(levels.values()) if index <= self.max_level]
        pg.draw.lines(self.screen, 'red', False, points, 6)
        
    def setup_icon(self):
        self.icon = GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def run(self):
        self.draw_paths()
        self.nodes.draw(self.screen)
        self.icon.draw(self.screen)
        
class Icon(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pg.Surface((20,20))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = pos)

class Node(Sprite):
    def __init__(self,pos,status):
        super().__init__()
        self.image = pg.Surface((100, 80))
        if status == 'available':
            self.image.fill('red')
        else:
            self.image.fill('gray')
        self.rect = self.image.get_rect(center = pos)