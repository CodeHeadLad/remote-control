def on_button_pressed_a():
    radio.send_string("centered")
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    radio.send_string("reverse")
    basic.show_arrow(ArrowNames.SOUTH)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    radio.send_string("left")
    basic.show_arrow(ArrowNames.WEST)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    radio.send_string("stop")
    basic.show_icon(IconNames.NO)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_tilt_right():
    radio.send_string("right")
    basic.show_arrow(ArrowNames.EAST)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    radio.send_string("forward")
    basic.show_arrow(ArrowNames.NORTH)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

radio.set_group(1)
radio.set_transmit_power(7)