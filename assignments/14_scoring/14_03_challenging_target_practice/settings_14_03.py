# I take my files from my main alien invasion project and adjust them based off the instructions from each exercise.

class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5

        # Bullet settings
        self.bullet_speed = 7
        self.bullet_width = 10
        self.bullet_height = 4
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Target settings
        self.target_speed = 3
        self.target_width = 50
        self.target_height = 150
        self.target_color = (200, 30, 30)
