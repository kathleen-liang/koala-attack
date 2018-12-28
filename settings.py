class Settings():
    """A class to store settings for Koala Attack"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_colour = (255, 255, 255)

        #Koala settings
        self.koala_speed_factor = 1.5
        self.koala_limit = 3

        #Leaf settings
        self.leaf_speed_factor = 1
        self.fleet_drop_speed = 10
        
        #fleet_direction of 1 is right, -1 is left
        self.fleet_direction = 1

        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 4
