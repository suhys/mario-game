import pygame as pg
import sys
from button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class LandingPage:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.landing_page_finished = False
        self.settings = game.settings
        self.highscore = game.stats.get_highscore()
        centerx = self.screen.get_rect().centerx
        
        self.font1 = pg.font.Font("font/Fixedsys500c.ttf", 50)
        self.font2 = pg.font.Font("font/Fixedsys500c.ttf", 30)
        
        strings = [
                  (f'Highest Score ={str(self.highscore)}', WHITE, self.font2)]
        
        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]
        self.posns = [450]
        
        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]
        
        self.background = pg.image.load(f'img/level/1-0.png')
        self.background = pg.transform.scale(self.background,
                                  (int(self.settings.screen_width*self.settings.background_multiplier),
                                  int(self.settings.screen_height)))

        self.icon = pg.transform.rotozoom(pg.image.load(f'img/landing_page/title_screen.png'),0,2)  
        self.icon_rect = self.icon.get_rect()
        self.center = (self.settings.screen_width/2, self.settings.screen_height/3)
        self.icon_rect.center = self.center

        self.play_button = Button(self.screen, "PLAY GAME", ul=(self.settings.screen_width/2, self.settings.screen_height -(self.settings.screen_height/3)))
        
        self.hover = False
        
    def get_text(self, font, msg, color): return font.render(msg, True, color)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect
    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])
    
    def mouse_on_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:   # pretend PLAY BUTTON pressed
                self.landing_page_finished = True        
            elif e.type == pg.MOUSEBUTTONDOWN:
                    if self.mouse_on_button():
                        self.landing_page_finished = True
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_button() and not self.hover:
                    self.play_button.toggle_colors()
                    self.hover = True
                elif not self.mouse_on_button() and self.hover:
                    self.play_button.toggle_colors()
                    self.hover = False
                    


    def show(self):
        while not self.landing_page_finished:
            self.draw()
            self.check_events()   # exits game if QUIT pressed


    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.icon, self.icon_rect)
        self.play_button.draw()
        self.draw_text()
        pg.display.flip()
