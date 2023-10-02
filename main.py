from random import randrange, random
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
PLAYER_SPEED = 5  # Adjust this value for player speed

class MyGame(arcade.Window):
    """Main application class"""

    def __init__(self, width, height):
        super().__init__(width, height, "My Arcade Game")

        arcade.set_background_color(arcade.color.AMAZON)

        # Initialize sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("mario-2d.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50  # Starting Position
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create the coins
        for i in range(COIN_COUNT):
            # create the coin instance
            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

            # positioning the coin
            coin.center_x = randrange(SCREEN_WIDTH)
            coin.center_y = randrange(SCREEN_HEIGHT)

            # add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()

        # Draw all the sprites
        self.coin_list.draw()
        self.player_list.draw()

        # Display the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """All the logic to move and the game logic goes here"""
        # Move the player based on the keyboard input
        if self.player_sprite.center_x >= 0 and self.player_sprite.center_x <= SCREEN_WIDTH:
            if self.right_pressed and not self.left_pressed:
                self.player_sprite.center_x += PLAYER_SPEED
            elif self.left_pressed and not self.right_pressed:
                self.player_sprite.center_x -= PLAYER_SPEED

        # Check for collisions with coins
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """Handle key press events"""
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Handle key release events"""
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def setup(self):
        """Setup the game and initialize variables"""
        self.left_pressed = False
        self.right_pressed = False

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
