from random import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

class MyGame(arcade.Window):
    """Main application class"""
    
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """Setup the game and initialize variables"""

        # Create the sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        
        # Score
        self.score = 0
        
        # Set up the player
        self.player_sprite = arcade.Sprite("mario-2d.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50 # Starting Position
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create the coins 
        for i in range(COIN_COUNT):
                # creating the coin instance
                coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

                # positioning the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # add the coin to the lists
                self.coin_list.append(coin)

    def on_draw(self):
        """Draw Everything"""
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        # generate a list of all coin sprites that collided with the player
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # loop through each colliding sprite, remove it and add to the score 
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()



















def draw_pine_tree(x, y):
    """This function draws a pine tree at the specified location"""

    # Draw the triangle on top of the trunk
    # We need three x, y points for the trianle
    arcade.draw_triangle_filled(x+40, y,  # Point1
                                x, y-100,  # Point2
                                x+80, y-100,  # Point3
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x+30, x+50, y-100, y-140,
                                      arcade.color.DARK_BROWN)
