import pygame
import sys
from settings import Settings

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                                self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()