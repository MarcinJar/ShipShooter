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
        
        # Bullet settings
        self.bullet_speed = 5.0  # Bullet movement speed in pixels per second
        self.bullet_width = 3  # Bullet width in pixels
        self.bullet_height = 10  # Bullet height in pixels
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # Number of bullets allowed on screen
        
        # alien settings
        self.alien_speed = 1.0  # Alien movement speed in pixels per second
        self.fleet_drop_speed = 10  # Alien drop speed in pixels per second
        self.fleet_direction = 1  # 1 for right, -1 for left
        
        