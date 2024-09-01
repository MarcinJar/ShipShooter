import sys
import pygame

from settings import Settings

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
        
    def run_game(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == '__main__':
    game = ShipShooter()
    game.run_game()
          

      