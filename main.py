from gpiozero import MotionSensor
from time import sleep
from pushbullet_message import send_alert

pir = MotionSensor(23)

TIMER_COUNTDOWN = 2


def motion_sensor_loop():
    while True:
        motion = pir.wait_for_motion(TIMER_COUNTDOWN)

        if motion:
            handle_signal_detected()
            pir.wait_for_no_motion()
        else:
            handle_countdown_completed()

        sleep(1)


def handle_signal_detected():
    """ Sends data to ThingSpeak """
    print('A Signal has been detected.')


def handle_countdown_completed():
    """ Sends a push-notification and sends data to ThingSpeak """
    print('The timer has ended')


motion_sensor_loop()
