class Settings:
    """
    A class to store all settings for the game.
    """
    
    def __init__(self):
        """
        Initialize the settings.
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (138, 43, 226)
        
        # Ship settings
        self.ship_speed = 2  # Ship movement speed in pixels per second
        