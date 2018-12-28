import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullets fired from koala"""
    def __init__(self, ka_settings, screen, koala):
        """Create bullet objects"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create bullet rect at (0, 0) and set to correct position
        self.rect = pygame.Rect(0, 0, ka_settings.bullet_width,
                                ka_settings.bullet_height)
        self.rect.centerx = koala.rect.centerx
        self.rect.top = koala.rect.top
        
        #Store bullet's position as decimal value
        self.y = float(self.rect.y)

        self.colour = ka_settings.bullet_colour
        self.speed_factor = ka_settings.bullet_speed_factor

    def update(self):
        """Move bullet up screen"""
        #Update decimal position of bullet
        self.y -= self.speed_factor
        #Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
