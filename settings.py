class Settings():
    """A class to store settings for Koala Attack"""

    def __init__(self):
        """Initialize game's static settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_colour = (255, 255, 255)

        #Koala settings
        self.koala_limit = 3

        #Leaf settings
        self.fleet_drop_speed = 10

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 4

        #Speed up of game
        self.speedup_scale = 1.1
        #How quickly leaf point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize game's dynamic settings"""
        self.koala_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.leaf_speed_factor = 1

        #Scoring
        self.leaf_points = 50

        #fleet_direction of 1 is right, -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and point values"""
        self.koala_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.leaf_speed_factor *= self.speedup_scale

        self.leaf_points = int(self.leaf_points * self.score_scale)
