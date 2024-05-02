def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_leds("""
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            """)
        servos.P0.set_angle(0)
        servos.P2.set_angle(180)
        music.play(music.builtin_playable_sound_effect(soundExpression.happy),
            music.PlaybackMode.UNTIL_DONE)
    if receivedNumber == 2:
        basic.show_leds("""
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            """)
        servos.P0.set_angle(180)
        servos.P2.set_angle(0)
        music.play(music.builtin_playable_sound_effect(soundExpression.sad),
            music.PlaybackMode.UNTIL_DONE)
    if receivedNumber == 3:
        servos.P0.stop()
        servos.P2.stop()
        basic.show_leds("""
            . . . . .
            # # . # #
            . . . . .
            . . . . .
            # # # # #
            """)
        music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
            music.PlaybackMode.UNTIL_DONE)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_number(3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
