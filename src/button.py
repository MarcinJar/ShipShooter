from __future__ import annotations 
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship_shooter import ShipShooter
    
class Button:
    def __init__(self, ss_game: ShipShooter, msg: str) -> None:
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self._prep_msg(msg)
        
    def _prep_msg(self, msg: str) -> None:
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self) -> None:
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)