from __future__ import annotations 
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship_shooter import ShipShooter

class Scoreboard:
    def __init__(self, ss_game: ShipShooter) -> None:
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()
        
    def prep_score(self) -> None:
        score_str = f"Score: {self.stats.score}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self) -> None:
        self.screen.blit(self.score_image, self.score_rect)