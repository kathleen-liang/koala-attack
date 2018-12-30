import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from gameStats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    #Create Play button
    play_button = Button(ka_settings, screen, "Play")

    #Create instance to store game stats and scoreboard
    stats = GameStats(ka_settings)
    sb = Scoreboard(ka_settings, screen, stats)

    #Make koala
    koala = Koala(ka_settings, screen)
    #Make group to store bullets
    bullets = Group()
    leaves = Group()

    #Create fleet of leaves
    gf.create_fleet(ka_settings, screen, koala, leaves)

    #Main loop
    while True:
        gf.check_events(ka_settings, screen, stats, sb, play_button, koala, leaves,
                        bullets)

        if stats.game_active:
            koala.update()
            gf.update_bullets(ka_settings, screen, stats, sb, koala, leaves, bullets)
            gf.update_leaves(ka_settings, screen, stats, sb, koala, leaves, bullets)

        gf.update_screen(ka_settings, screen, stats, sb, koala, leaves, bullets,
                         play_button)

run_game()
