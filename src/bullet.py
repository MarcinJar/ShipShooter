from __future__ import annotations 
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship_shooter import ShipShooter

class Bullet(Sprite):
    def __init__(self, ss_game: ShipShooter) -> None:
        """
        Initialize the bullet and set its starting position.
        Args:
        ss_game (ShipShooter): An instance of the main game class.
        """
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ss_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self) -> None:
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.rect)
