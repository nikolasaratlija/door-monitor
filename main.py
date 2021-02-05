from gpiozero import MotionSensor
from time import sleep
from pushbullet_message import send_alert
from thingspeak_sender import send_motion_data, send_alert_data

# Sets up the MotionSensor object.
# 23 is the pin that's been connected to the sensor.
pir = MotionSensor(23)

# Amount of time that's waited before the program sends a notification to the user.
TIMER_COUNTDOWN = 15


def handle_motion_detected():
    """ Sends data to ThingSpeak """
    print('Motion Detected')
    send_motion_data()


def handle_timeout_reached():
    """ Sends a push-notification and sends data to ThingSpeak """
    print('Sending a push-notification')
    send_alert_data()
    send_alert()


def motion_sensor_loop():
    while True:
		# Pauses the script until motion gets detected, or timout completes
		# Returns True when motion is detected, false otherwise
        motion = pir.wait_for_motion(TIMER_COUNTDOWN)

        if motion:
            handle_motion_detected()
            '''
            The sensor keeps outputting 1 after a signal has been 
            detected for a specified amount of time, based on the 
            potentiometer. The following line pauses the script until
            the sensor outputs 0 again. 
            '''
            pir.wait_for_no_motion()
        else:
            handle_timeout_reached()

        sleep(1)


print('Motion Detection Started')
motion_sensor_loop()
