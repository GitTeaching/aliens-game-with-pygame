import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inialize game, setting, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Ship instance
    ship = Ship(ai_settings, screen)
    
    # Start the main loop of the game
    while True:
        
        # Watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        
        # Redraw the screen during each pass through the loop - with background color      
        #Ship on the screen    
        #Make the most recently drwan screen visible
        gf.update_screen(ai_settings, screen, ship)


run_game()