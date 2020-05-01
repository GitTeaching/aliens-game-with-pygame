import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               check_keydown_events(event, ai_settings, screen, ship, bullets)
            
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Respond to keypress
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def update_screen(ai_settings, screen, ship, bullets):
    # Redraw the screen during each pass through the loop - with background color
    screen.fill(ai_settings.bg_color)  
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Ship on the screen
    ship.blitme()        
    #Make the most recently drwan screen visible
    pygame.display.flip()

def update_bullets(bullets):    
    # Update bullet positions
    bullets.update() 
    # Get rid of bullets taht have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)