import time, sys
from distances.dist_measure import *
from distances.dist_angle import *
from threading import Thread
from communication.com_serial import SerialComm


class BackAppRPi:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.servo_obj_list = Angles(servo_pin=12)
        self.us_obj_list = Measure(trig=23, echo=24)

        self.ser_get_angle = SerialComm(port="/dev/ttyUSB0", name="Dist_Fetcher", baudrate=115200)
        self.t_get_dist_asynch = Thread(target=self.angle_fetcher, args=[], daemon=True)
        self.angle_list = [-1]
        self.dist_list = [-1]
        self.thread_activated = False

    def orient(self):
        while True:
            if not self.thread_activated:
                self.thread_activated = True
                self.t_get_dist_asynch.start()

            if self.angle_list[0] != -1:
                print(f"Angle to be applied on Servo : {self.angle_list[0]}")
                self.servo_obj_list[0].set_angle(self.angle_list[1])
                self.dist_list[0] = self.us_obj_list[0].distance_read()

            print(f'angle_list {self.angle_list}')
            print(f'dist_list {self.dist_list}')
            self.ser_get_angle.send_query(self.dist_list)
            time.sleep(1)

    def angle_fetcher(self):
        while True:
            self.angle_list = [section for section in self.ser_get_angle.receive_query()]
            time.sleep(0.3)


run = BackAppRPi()
run.orient()
