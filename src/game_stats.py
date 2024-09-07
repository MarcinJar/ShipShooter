from __future__ import annotations 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship_shooter import ShipShooter

class GameState:
    def __init__(self, ss_game: ShipShooter):
        self.settings = ss_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        self.ships_left = self.settings.ships_limit