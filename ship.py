from __future__ import annotations 
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship_shooter import ShipShooter

class Ship:
    def __init__(self, ss_game: ShipShooter) -> None:
        """
        Initialize the ship and set its starting position.
        Args:
            ss_game (ShipShooter): An instance of the ShipShooter game.
        """
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.image = pygame.image.load('images/DurrrSpaceShip.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self) -> None:
        """
        Draw the ship at its current location.
        This method uses the `blit` function from the pygame library to draw the ship's image onto the screen.
        The ship's image is drawn at the position specified by the ship's rectangle.
        """
        self.screen.blit(self.image, self.rect)

        