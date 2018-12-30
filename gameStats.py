class GameStats():
    """Tracks stats for Koala Attack"""

    def __init__(self, ka_settings):
        """Initialize statistics"""
        self.ka_settings = ka_settings
        self.reset_stats()
        #Start in active state
        self.game_active = False
        #High score
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that change during game"""
        self.koalas_left = self.ka_settings.koala_limit
        self.score = 0
        self.level = 1
