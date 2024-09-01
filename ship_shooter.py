import sys
import pygame

from settings import Settings
from ship import Ship

class ShipShooter:
    """
    General class for managing resources and the way of working with the game.
    This class initializes the game and sets up the necessary resources.
    """

    def __init__(self) -> None:
        """
        Initialize the game.
        This function initializes the pygame module, which is necessary for creating the game window and handling game events.
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        width = self.settings.screen_width
        height = self.settings.screen_height
        self.screen = pygame.display.set_mode((width, height))
        
        self.ship = Ship(self)

    def run_game(self) -> None:
        """
        Run the main loop for the game.
        This function contains an infinite loop that runs the game. It checks for events, updates the screen, and limits the frame rate.
        """
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self) -> None:
        """
        Check for keyboard events and update the ship's position accordingly.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
    
    def _update_screen(self) -> None:
        """
        Update the screen with the new position of the ship.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    game = ShipShooter()
    game.run_game()

          

      