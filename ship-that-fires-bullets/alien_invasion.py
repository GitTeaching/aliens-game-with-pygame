import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Inialize game, setting, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Ship instance
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets in
    bullets = Group()
    
    # Start the main loop of the game
    while True:
        
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        
        gf.update_bullets(bullets)
        
        # Redraw the screen during each pass through the loop - with background color      
        #Ship on the screen    
        #Make the most recently drwan screen visible
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()