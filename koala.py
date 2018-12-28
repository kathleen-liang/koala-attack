import pygame

class Koala():
    def __init__(self, ka_settings, screen):
        """Initialize koala at starting position"""
        self.screen = screen
        self.ka_settings = ka_settings

        #Load koala image
        self.image = pygame.image.load('images/koala.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start every new koala at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal value for koala's center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update koala's movement according to flag"""
        #Update koala's center value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ka_settings.koala_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ka_settings.koala_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw koala at current location"""
        self.screen.blit(self.image, self.rect)

    def center_koala(self):
        """Center koala"""
        self.center = self.screen_rect.centerx
