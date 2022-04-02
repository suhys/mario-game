class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset_stats()
        self.game_active = True
        self.score = 0
        self.highscore = 0
        self.highscore = self.load_high_score()