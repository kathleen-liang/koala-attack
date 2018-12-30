import pygame.font
from pygame.sprite import Group

from koala import Koala

class Scoreboard():
    """Class to report scoring information"""

    def __init__(self, ka_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ka_settings = ka_settings
        self.stats = stats

        #Font settings
        self.text_colour = (30, 30 ,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score
        self.prep_score()
        self.prep_high_score()
        
        self.prep_level()
        self.prep_koalas()

    def prep_score(self):
        """Turn score into image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score: " + score_str, True, self.text_colour,
                                            self.ka_settings.bg_colour)


        #Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - self.score_rect.top
        
        
    def prep_high_score(self):
        """Turn high score into image"""
        high_score = int(round(self.stats.score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("High: " + high_score_str, True,
                                                 self.text_colour,
                                                 self.ka_settings.bg_colour)


        #Display score at top right
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        
        self.screen.blit(self.level_image, self.level_rect)
        self.koalas.draw(self.screen)

    def prep_level(self):
        """Turn level into image"""
        self.level_image = self.font.render("Lvl: " + str(self.stats.level), True,
                                            self.text_colour,
                                            self.ka_settings.bg_colour)

        #Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        beneath_score = 10
        self.level_rect.top = self.score_rect.bottom + beneath_score

    def prep_koalas(self):
        """Show koals left"""
        self.koalas = Group()
        for koala_number in range(self.stats.koalas_left):
            koala = Koala(self.ka_settings, self.screen)
            koala.rect.x = 10 + koala_number * koala.rect.width
            koala.rect.y = 10
            self.koalas.add(koala)
        
