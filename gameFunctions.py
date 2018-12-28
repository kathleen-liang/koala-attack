import sys
from time import sleep

import pygame

from bullet import Bullet
from leaf import Leaf

def get_number_leaves_x(ka_settings, leaf_width):
    """Determine number of leaves in a row"""
    available_space_x = ka_settings.screen_width - 2 * leaf_width
    number_leaves_x = int(available_space_x / (2 * leaf_width))
    return number_leaves_x

def get_number_rows(ka_settings, koala_height, leaf_height):
    """Determine number of rows of leaves"""
    available_space_y = ka_settings.screen_height - 3 * leaf_height - koala_height
    number_rows = int(available_space_y / (2 * leaf_height))
    return number_rows

def create_leaf(ka_settings, screen, leaves, leaf_number, row_number):
    """Create leaf and place in row"""
    leaf = Leaf(ka_settings, screen)
    leaf_width = leaf.rect.width
    leaf.x = leaf_width + 2 * leaf_width * leaf_number
    leaf.rect.x = leaf.x
    leaf.rect.y = leaf.rect.height + 2 * leaf.rect.height * row_number
    leaves.add(leaf)    
    
def create_fleet(ka_settings, screen, koala, leaves):
    """Create fleet of leaves"""
    #Create leaf and find number of leaves in row
    #Spacing is one width of a leaf
    leaf = Leaf(ka_settings, screen)
    number_leaves_x = get_number_leaves_x(ka_settings, leaf.rect.width)
    number_rows = get_number_rows(ka_settings, koala.rect.height, leaf.rect.height)

    #Create fleet of leaves
    for row_number in range(number_rows):
        for leaf_number in range(number_leaves_x):
            create_leaf(ka_settings, screen, leaves, leaf_number, row_number)

def check_fleet_edges(ka_settings, leaves):
    """Respond if aliens reach an edge"""
    for leaf in leaves.sprites():
        if leaf.check_edges():
            change_fleet_direction(ka_settings, leaves)
            break

def change_fleet_direction(ka_settings, leaves):
    """Drop entire fleet and change direction"""
    for leaf in leaves.sprites():
        leaf.rect.y += ka_settings.fleet_drop_speed
    ka_settings.fleet_direction *= -1

def update_leaves(ka_settings, stats, screen, koala, leaves, bullets):
    """Check if fleet is at edge and update positions of leaves"""
    check_fleet_edges(ka_settings, leaves)
    leaves.update()

    #Look for leaf and koala collisions
    if pygame.sprite.spritecollideany(koala, leaves):
        koala_hit(ka_settings, stats, screen, koala, leaves, bullets)

    #Look for leaves hitting screen bottom
        check_leaves_bottom(ka_settings, stats, screen, koala, leaves, bullets)

def koala_hit(ka_settings, stats, screen, koala, leaves, bullets):
    if stats.koalas_left > 0:
        """Respond to koala being hit by leaf"""
        stats.koalas_left -= 1

        #Empty list of leaves and bullets
        leaves.empty()
        bullets.empty()

        #Create new fleet and center koala
        create_fleet(ka_settings, screen, koala, leaves)
        koala.center_koala()

        #Pause
        sleep(0.5)
    else:
        stats.game_active = False

def check_keydown_events(event, ka_settings, screen, koala, bullets):
    if event.key == pygame.K_RIGHT:
        #Move koala to right
        koala.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move koala to left
        koala.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ka_settings, screen, koala, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ka_settings, screen, koala, bullets):
    """Fire bullet if limit not reached"""
    #Create bullet and add to bullets group
    if len(bullets) < ka_settings.bullets_allowed:
        new_bullet = Bullet(ka_settings, screen, koala)
        bullets.add(new_bullet)


def check_keyup_events(event, koala):
    if event.key == pygame.K_RIGHT:
        koala.moving_right = False
    elif event.key == pygame.K_LEFT:
        koala.moving_left = False
    
def check_events(ka_settings, screen, koala, bullets):
    """Repond to mouse and key presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ka_settings, screen, koala, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, koala)

    
def update_bullets(ka_settings, screen, koala, leaves, bullets):
    """Update position of bullets and gets rid of old bullets"""
    #Update bullet position
    bullets.update()

    #Gets rid of bullets that disappear
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_leaf_collisions(ka_settings, screen, koala, leaves, bullets)

def check_bullet_leaf_collisions(ka_settings, screen, koala, leaves, bullets):
    #Checks if bullet has hit leaf
    collisions = pygame.sprite.groupcollide(bullets, leaves, True, True)

    if len(leaves) == 0:
        #Destroy existing bullets and create new fleet
        bullets.empty()
        create_fleet(ka_settings, screen, koala, leaves)

def check_leaves_bottom(ka_settings, stats, screen, koala, leaves, bullets):
    """Check if leaves have reached screen bottom"""
    screen_rect = screen.get_rect()
    for leaf in leaves.sprites():
        if leaf.rect.bottom >= screen_rect.bottom:
            koala_hit(ka_settings, stats, screen, koala, leaves, bullets)
            break
            
def update_screen(ka_settings, screen, koala, leaves, bullets):
        #Redraw screen
        screen.fill(ka_settings.bg_colour)
        #Redraw bullets behind koalas and leaves
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        koala.blitme()
        leaves.draw(screen)
        
        #Show drawn screen
        pygame.display.flip()
