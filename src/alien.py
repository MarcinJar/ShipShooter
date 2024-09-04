from __future__ import annotations 
import pygame
from typing import TYPE_CHECKING
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from ship_shooter import ShipShooter

class Alien(Sprite):
    def __init__(self, ss_game: ShipShooter):
        super().__init__()
        self.screen = ss_game.screen
        
        image = pygame.image.load('./images/DurrrSpaceShip.png')

        # Get the original dimensions of the image
        original_width, original_height = image.get_size()

        # Calculate the new dimensions (half of the original size)
        new_width = original_width * 3 // 4
        new_height = original_height * 3 // 4

        # Resize the image to half of its original size
        resized_image = pygame.transform.scale(image, (new_width, new_height))

        # Rotate the resized image by 180 degrees (optional)
        self.image = pygame.transform.rotate(resized_image, 180)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height - 20
        
        self.x = float(self.rect.x)
        
        
        
        