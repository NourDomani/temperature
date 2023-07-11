input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (input.temperature() > 25) {
        basic.showNumber(input.temperature())
        basic.showIcon(IconNames.Meh)
        basic.pause(4000)
        basic.showString("HOT")
    } else {
        basic.showNumber(input.temperature())
        basic.showLeds(`
            . . # # #
            . # . . .
            . # . . .
            . # . . .
            . . # # #
            `)
        basic.pause(2000)
        basic.showString("Very Cold")
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showArrow(ArrowNames.East)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("Micro.bit")
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("earthquick")
})
