import time
from mathematics.mathlib import map_values_ranges
import RPi.GPIO as GPIO


class Angles:
    def __init__(self, servo_pin):
        GPIO.setup(servo_pin, GPIO.OUT)
        self.servo_pin = servo_pin

        # GPIO 17 for PWM with 50Hz
        self.pwm_ch = GPIO.PWM(servo_pin, 50)
        self.pwm_ch.start(2.5)  # Initialization

    def set_angle(self, angle):
        self.pwm_ch.ChangeDutyCycle(map_values_ranges(angle, 180, 0, 2, 12))
        