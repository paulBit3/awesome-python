import sys

import pygame


from modules.settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # running the game in fullscreen mode...to implement soon...

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Storing Bullets in a Group
        self.bullets = pygame.sprite.Group()

        # we create a Group to hold the fleet of aliens
        self.aliens = pygame.sprite.Group()

        # and we call _create_fleet() method
        self._create_fleet()

        # Setting the background color
        self.bg_color = (230, 230, 230)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size  # size contains a tuple with the width and height of a rect object
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            # Creating the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)  # calling the helper method

    # Building the Alien Fleet
    # Adding a new helper method
    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  # size contains a tuple with the width and height of a rect object
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self.ship.update()
            self._update_bullets()  # update the position of the bullets on each pass
            self._update_aliens()
            self._update_screen()

    # Manage events and refactoring code
    def _check_events(self):
        """responding to a keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                # self.ship.rect.x += 1  # Move the ship to the right
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    """refactoring the _check_events() method """

    # Handling KEYDOWN event
    def _check_keydown_events(self, event):
        """Response to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # Pressing Q to Quit the game
            sys.exit()
        elif event.key == pygame.K_SPACE:  # Fire a bullet when te player press the Spacebar
            self._fire_bullet()

    # Handling KEYUP event
    def _check_keyup_events(self, event):
        """Response to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    # Creating the update bullets method to manage bullet
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    # Manage the movement of the fleet
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self.aliens.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)  # To make the alien appear, we call the group's draw method
        """Make the most recently drawn screen visible."""
        pygame.display.flip()


if __name__ == '__main__':
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()