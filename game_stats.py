from level import GameLevel

class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.game_active = True
        self.score = 0
        self.highscore = 0
        self.coin_score = 0
        self.highscore = self.load_high_score()
        self.mario_left = self.settings.mario_limit
        self.last_mario_left = self.mario_left
        self.level = self.settings.current_level
    
    def get_mario_left(self): return self.mario_left
    
    def mario_die(self):
        self.mario_left -= 1
        n = self.mario_left
        print(f'Mario Die!', end=' ')
        if self.last_mario_left != self.mario_left:
            print(f'{self.mario_left} ship{"s" if n != 1 else ""} left')
            self.last_mario_left = self.mario_left
    
    def get_score(self): return self.score
    def get_highscore(self): return self.highscore
    def get_coin_score(self): return self.coin_score
    def get_level(self): return self.level
    
    def __del__(self): self.save_high_score()
    
    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
                return 0
                       
    def save_high_score(self):
        print("in save_high_score()")
        try:
            with open("highscore.txt", "w+") as f:
                f.write(str(round(self.highscore, -1)))
        except:
            print("highscore.txt not found...")
            
    def score_update(self):
        self.score += self.coin_score
        self.highscore = max(self.score, self.highscore)