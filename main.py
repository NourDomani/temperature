def on_button_pressed_a():
    if input.temperature() > 25:
        basic.show_number(input.temperature())
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.pause(5000)
        basic.show_string("HOT")
    else:
        basic.show_number(input.temperature())
        basic.show_string("Very Cold")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_arrow(ArrowNames.SOUTH)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Hello!")
input.on_button_pressed(Button.B, on_button_pressed_b)