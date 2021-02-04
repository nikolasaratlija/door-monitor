import time
from random import randint

TIMER_COUNTDOWN = 5


def timer_loop():
    signal = False
    alarm = False
    seconds_passed = 0

    while signal is False and alarm is False:
        signal_result = randint(1, 5)

        if signal_result == 1:
            # A Signal has been detected
            signal = True
            handle_signal_detected()
        elif seconds_passed == TIMER_COUNTDOWN:
            # Timer has counted down
            alarm = True
            handle_countdown_completed()

        print('Seconds passed: ', seconds_passed, ' | Signal: ', signal)

        if signal or alarm:
            # Resets the timer
            timer_loop()

        time.sleep(1)
        seconds_passed += 1


def handle_signal_detected():
    """ Instructions for when a signal has been detected"""
    print('A Signal has been detected.')


def handle_countdown_completed():
    """ Instructions for when the timer has ended """
    print('The timer has ended')
