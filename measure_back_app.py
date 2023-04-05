import time, sys
from distances.dist_measure import *
from distances.dist_angle import *
from threading import Thread
from communication.com_serial import SerialComm


class BackAppRPi:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.servo_obj_list = [Angles(servo_pin=12)]
        self.us_obj_list = [Measure(trig=23, echo=24)]

        self.ser_get_angle = SerialComm(port="/dev/ttyUSB0", name="Dist_Fetcher", baudrate=115200)
        self.t_get_dist_asynch = Thread(target=self.angle_fetcher, args=[], daemon=True)
        self.angle_list = [-1, -1, -1]
        self.dist_list = [-1, -1, -1]
        self.thread_activated = False

    def orient(self):
        while True:
            if not self.thread_activated:
                self.thread_activated = True
                self.t_get_dist_asynch.start()

            print(f"Angle to be applied on Servo : {self.angle_list[0]}")
            self.servo_obj_list[0].set_angle(self.angle_list[1])
            self.dist_list[0] = self.us_obj_list[0].distance_read()

            print(f'angle_list {self.angle_list}')
            print(f'dist_list {self.dist_list}')
            self.ser_get_angle.send_query(self.dist_list)
            time.sleep(1)

    def angle_fetcher(self):
        while True:
            received = self.ser_get_angle.receive_query()
            if received["ORIENT"] != [-1, -1, -1]:
                last_received = received
                self.angle_list = [section for section in last_received["ORIENT"]]
                for i in range(0, 3):
                    if self.angle_list[i] < 0:
                        if i == 0:
                            self.angle_list[i] = 45
                        elif i == 1:
                            self.angle_list[i] = 90
                        elif i == 2:
                            self.angle_list[i] = 135
            print(f"Debug: received App: {self.angle_list}")
            time.sleep(0.3)


run = BackAppRPi()
run.orient()

