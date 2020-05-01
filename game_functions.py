import sys
import pygame

def check_events(ship):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass through the loop - with background color
    screen.fill(ai_settings.bg_color)      
    #Ship on the screen
    ship.blitme()        
    #Make the most recently drwan screen visible
    pygame.display.flip()