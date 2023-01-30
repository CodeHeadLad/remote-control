input.onButtonPressed(Button.A, function () {
    radio.sendString("centered")
    basic.showArrow(ArrowNames.North)
})
input.onGesture(Gesture.LogoUp, function () {
    radio.sendString("reverse")
    basic.showArrow(ArrowNames.South)
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendString("left")
    basic.showArrow(ArrowNames.West)
})
input.onGesture(Gesture.ScreenUp, function () {
    radio.sendString("stop")
    basic.showIcon(IconNames.No)
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendString("right")
    basic.showArrow(ArrowNames.East)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendString("forward")
    basic.showArrow(ArrowNames.North)
})
radio.setGroup(1)
radio.setTransmitPower(7)
