import time, cv2, sys

from distances.dist_measure import *
from distances.dist_angle import *
from threading import Thread
from communication.com_serial import SerialComm

class FrontAppRPi:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.servo_obj_list = [Angles(servo_pin=18), Angles(servo_pin=12), Angles(servo_pin=13)]
        self.us_obj_list = [Measure(trig=27, echo=22), Measure(trig=23, echo=24), Measure(trig=5, echo=6)]

        self.ser_get_angle = SerialComm(port="/dev/ttyUSB0", name="Dist_Fetcher", baudrate=115200)
        self.t_get_dist_asynch = Thread(target=self.angle_fetcher, args=[], daemon=True)
        self.angle_list = [-1, -1, -1]
        self.dist_list = [-1, -1, -1]
        self.thread_activated = False
        
        
    def orinet(self):
        while True:
            if not self.thread_activated:
                self.thread_activated = True
                self.t_get_dist_asynch.start()
                
            for section in range(0, 3):
                print(f"Angle to be applied on Servo {1+section} : {self.angle_list[section]}")
                self.servo_obj_list[section].set_angle(self.angle_list[section])
                self.dist_list[section] = self.us_obj_list[section].distance_read()
            
            print(f'angle_list {self.angle_list}')
            print(f'dist_list {self.dist_list}')
            self.ser_get_angle.send_query(self.dist_list)
            time.sleep(1)

    def angle_fetcher(self):
        while True:
            self.angle_list = [section for section in self.ser_get_angle.receive_query()]
            time.sleep(0.3)


run = FrontAppRPi()
run.orinet()