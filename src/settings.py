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
        self.ship_limit = 3  # Number of ships allowed on screen
        
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
        
        self.speedup_scale = 1.1  # Speed-up multiplier
        self.initial_ship_speed = 1.5  # Initial ship speed
        self.initial_bullet_speed = 3.0  # Initial bullet speed
        self.initial_alien_speed = 0.5  # Initial alien speed
        self.initial_fleet_drop_speed = 5  # Initial alien drop speed
        
        self.alien_points = 50  # Points for destroying an alien
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game.
        """
        self.ship_speed = self.initial_ship_speed * self.speedup_scale
        self.bullet_speed = self.initial_bullet_speed * self.speedup_scale
        self.alien_speed = self.initial_alien_speed * self.speedup_scale
        self.fleet_drop_speed = self.initial_fleet_drop_speed * self.speedup_scale
        
    def increase_speed(self):
        """
        Increase the speed settings by a factor of speedup_scale.
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        
    def set_easy_level(self):
        self.ship_speed = self.initial_ship_speed * self.speedup_scale
        self.bullet_speed = self.initial_bullet_speed * self.speedup_scale
        self.alien_speed = self.initial_alien_speed * self.speedup_scale
        self.fleet_drop_speed = self.initial_fleet_drop_speed * self.speedup_scale
        
    def set_medium_level(self):
        self.ship_speed *= 3
        self.bullet_speed = 3
        self.alien_speed *= 3
        self.fleet_drop_speed *= 3
        
    def set_hight_level(self):
        self.ship_speed *= 8
        self.bullet_speed = 8
        self.alien_speed *= 8
        self.fleet_drop_speed *= 8
        
        