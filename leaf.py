import pygame
from pygame.sprite import Sprite

class Leaf(Sprite):
    """Class to represent single leaf"""

    def __init__(self, ka_settings, screen):
        """Initialize leaf to position"""
        super(Leaf, self).__init__()
        self.screen = screen
        self.ka_settings = ka_settings

        #Load leaf image and set rect attribute
        self.image = pygame.image.load('images/leaf.bmp')
        self.rect = self.image.get_rect()

        #Start leaf at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store alien's position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw leaf at current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move leaf right/left"""
        self.x += (self.ka_settings.leaf_speed_factor
                   * self.ka_settings.fleet_direction)
        self.rect.x = self.x
                                       
