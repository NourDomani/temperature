input.onButtonPressed(Button.A, function () {
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
input.onButtonPressed(Button.AB, function () {
    basic.showArrow(ArrowNames.South)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Hello!")
})
