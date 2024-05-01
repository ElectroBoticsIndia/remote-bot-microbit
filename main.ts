radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            `)
        servos.P0.setAngle(0)
        servos.P2.setAngle(180)
        music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
    }
    if (receivedNumber == 2) {
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            `)
        servos.P0.setAngle(180)
        servos.P2.setAngle(0)
        music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.UntilDone)
    }
    if (receivedNumber == 3) {
        servos.P0.stop()
        servos.P2.stop()
        basic.showLeds(`
            . . . . .
            # # . # #
            . . . . .
            . . . . .
            # # # # #
            `)
        music.play(music.builtinPlayableSoundEffect(soundExpression.yawn), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})
input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(3)
})
radio.setGroup(1)
basic.forever(function () {
	
})
