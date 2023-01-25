def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    Kitronik_Game_Controller.run_motor(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
