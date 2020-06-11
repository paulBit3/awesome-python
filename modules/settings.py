import os
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

"""The settings module"""

class Settings:
    """A class to store all settings for our game"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3   # Limiting the Number of Bullets

        # Alien settings
        self.alien_speed = 1.0