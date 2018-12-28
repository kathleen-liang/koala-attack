import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from gameStats import GameStats
from koala import Koala
from leaf import Leaf
import gameFunctions as gf

def run_game():
    #Start game and create object on screen
    pygame.init() #initializes background settings
    ka_settings = Settings()
    screen = pygame.display.set_mode((ka_settings.screen_width,
                                      ka_settings.screen_height)) 
    pygame.display.set_caption("Koala Attack")

    #Create instance to store game stats
    stats = GameStats(ka_settings)

    #Make koala
    koala = Koala(ka_settings, screen)
    #Make group to store bullets
    bullets = Group()
    leaves = Group()

    #Create fleet of leaves
    gf.create_fleet(ka_settings, screen, koala, leaves)

    #Main loop
    while True:
        gf.check_events(ka_settings, screen, koala, bullets)

        if stats.game_active:
            koala.update()
            gf.update_bullets(ka_settings, screen, koala, leaves, bullets)
            gf.update_leaves(ka_settings, stats, screen, koala, leaves, bullets)

        gf.update_screen(ka_settings, screen, koala, leaves, bullets)

run_game()
