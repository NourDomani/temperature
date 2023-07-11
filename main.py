def on_button_pressed_a():
    if input.temperature() > 25:
        basic.show_number(input.temperature())
        basic.show_icon(IconNames.MEH)
        basic.pause(4000)
        basic.show_string("HOT")
    else:
        basic.show_number(input.temperature())
        basic.show_leds("""
            . . # # #
            . # . . .
            . # . . .
            . # . . .
            . . # # #
            """)
        basic.pause(2000)
        basic.show_string("Very Cold")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_arrow(ArrowNames.EAST)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Micro.bit")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("earthquick")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
