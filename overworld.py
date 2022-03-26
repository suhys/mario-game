import pygame as pg
from game_data import levels
from pygame.sprite import Group, Sprite


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
        
    def setup_nodes(self):
        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available')
            else:
                node_sprite = Node(node_data['node_pos'], 'locked')
            self.nodes.add(node_sprite)

    def run(self):
        self.nodes.draw(self.screen)

class Node(Sprite):
    def __init__(self,pos, status):
        super().__init__()
        self.image = pg.Surface((100, 80))
        if status == 'available':
            self.image.fill('red')
        else:
            self.image.fill('gray')
        self.rect = self.image.get_rect(center = pos)