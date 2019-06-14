import arcade
import time


WIDTH = 640
HEIGHT = 480


space_clicked = False
space_released = False
player_y_reset = 0
player_x_reset = -100
player_alive = True
current_screen = "menu"
player_loc = [-100, 0]
x_rectangle = 100

keys_pressed = {arcade.key.RIGHT: False}


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Geometry Dash Remake")
    arcade.schedule(update, 1/60)
    arcade.set_viewport(-WIDTH / 2, WIDTH / 2, -HEIGHT / 2, HEIGHT / 2)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_pressed
    window.on_key_release = on_key_release

    arcade.run()

def update(delta_time):
    global space_clicked, space_released, player_y_reset, player_loc, keys_pressed, player_alive
    if keys_pressed[arcade.key.RIGHT]:
        player_loc[0] += 4
    if space_clicked == True:
        player_loc[1] += 40
        player_loc[0] += 10
    elif space_clicked == False:
        player_loc[1] = player_y_reset

    for i in range(20):
        x = x_rectangle + i * 300
        w = 50
        h = 70
        if player_loc[0] >= x and player_loc[0] <= x + w and player_loc[1] <= h:
            player_alive = False
            player_loc[0] = player_x_reset



def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        main_menu()
    elif current_screen == "instructions":
        instructions_screen()
    elif current_screen == "play":
        play_screen()

def on_key_pressed(key, modifiers):
    global space_clicked, current_screen, keys_pressed
    if key == arcade.key.SPACE:
        space_clicked = True
    if current_screen == "menu":
        if key == arcade.key.I:
            current_screen = "instructions"
        elif key == arcade.key.P:
            current_screen = "play"
    elif current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
            arcade.set_viewport(0, WIDTH, 0, HEIGHT)
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    keys_pressed[key] = True

def on_key_release(key, modifiers):
    global space_clicked, space_released, keys_pressed
    if key == arcade.key.SPACE:
        space_clicked = False
        space_released = True
    keys_pressed[key] = False


def main_menu():
    arcade.set_background_color(arcade.color.ORANGE_RED)
    arcade.draw_text("GEOMETRY DASH", WIDTH / 2 - 160, 400, arcade.color.BLACK, 30)
    arcade.draw_text("Main Menu", WIDTH / 2 - 80, 300, arcade.color.BLACK, 20)
    arcade.draw_text("I for Instructions", WIDTH / 2 - 100, HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20)
    arcade.draw_text("P to play", WIDTH / 2 - 70, HEIGHT / 2 - 120, arcade.color.BLACK, font_size=20)



def instructions_screen():
    arcade.set_background_color(arcade.color.ALLOY_ORANGE)
    arcade.draw_text("Instructions", WIDTH / 2 - 110, HEIGHT / 2 + 100, arcade.color.BLACK, font_size=30)
    arcade.draw_text("Use space to make the square jump and avoid all obstacles!!",
                     WIDTH / 2 - 300, HEIGHT / 2, arcade.color.BLACK, 15)
    arcade.draw_text("Hold the right key to move to the right", WIDTH/2 - 160, HEIGHT/2 - 50, arcade.color.BLACK, 15)
    arcade.draw_text("ESC to go back", WIDTH / 2 - 100, HEIGHT / 2 - 100, arcade.color.BLACK, font_size=20)


def play_screen():
    global player_loc, keys_pressed, x_rectangle, player_x_reset, player_alive
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.draw_text("GEOMETRY DASH", WIDTH / 2 - 160, 400, arcade.color.BLACK, 30)
    arcade.draw_rectangle_filled(player_loc[0] + 33, player_loc[1] + 23, 60, 60, arcade.color.YELLOW)
    for i in range(20):
        x = x_rectangle + i*300
        y = -20
        w = 50
        h =70
        arcade.draw_xywh_rectangle_filled(x, y, w, h, arcade.color.BLACK)

    arcade.draw_text("ESC to go back", 540, 400, arcade.color.BLACK, 10)
    arcade.set_viewport(-WIDTH / 2 + player_loc[0] + 320,
                        WIDTH / 2 + player_loc[0] + 320,
                        -HEIGHT / 2 + player_loc[1] + 230,
                        HEIGHT / 2 + player_loc[1] + 230)




if __name__ == '__main__':
    setup()
