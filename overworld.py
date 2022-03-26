import pygame as pg
from game_data import levels

class Overworld:
    def __init__(self, game):
        #setup
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.max_level = self.settings.max_level
        self.current_level = self.settings.start_level
        
    def run(self):
        pass