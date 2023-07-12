import time, sys
from distances.dist_measure import *
from distances.dist_angle import *
from threading import Thread
from communication.com_serial import SerialComm


class FrontAppRPi:
    TOTAL_VIEW = 180
    def __init__(self):
        self.resolutoin = 15
        GPIO.setmode(GPIO.BCM)
        self.servo_obj_list = Angles(servo_pin=18)
        self.us_obj_list = Measure(trig=27, echo=22)

        self.ser_get_angle = SerialComm(port="/dev/ttyUSB0", name="Dist_Fetcher", baudrate=115200)
        self.t_get_dist_asynch = Thread(target=self.angle_scanner, args=[], daemon=True)
        self.angle_list = [FrontAppRPi.TOTAL_VIEW/self.resolutoin * step for step in range(0, self.resolutoin+1)]
        print(f"Total angles: {self.angle_list}")
        self.dist_list = [-1] * self.resolutoin
        self.thread_activated = False

    def periodic_update(self):
        while True:
            if not self.thread_activated:
                self.thread_activated = True
                self.t_get_dist_asynch.start()
            print(f'dist_list {self.dist_list}')
            self.ser_get_angle.send_query({"DISTANCE": self.dist_list})
            time.sleep(0.6)

    def angle_scanner(self):
        while True:
            self.angle_orientCW()
            self.angle_orientCCW()
            

            print(f'angle_list {self.angle_list}')
    def angle_orientCW (self):
        for scan_angle in range(0, self.resolutoin):
            print(f"Angle {scan_angle} to orient Servo")
            self.servo_obj_list.set_angle(self.angle_list[scan_angle])
            #time.sleep(0.05)
            self.dist_list[scan_angle] = self.us_obj_list.distance_read()
            time.sleep(0.1)

    def angle_orientCCW (self):
        for scan_angle in range(0, self.resolutoin):
            print(f"Angle {scan_angle} to orient Servo")
            self.servo_obj_list.set_angle(self.angle_list[self.resolutoin - scan_angle - 1])
            #time.sleep(0.05)
            self.dist_list[self.resolutoin - scan_angle - 1] = self.us_obj_list.distance_read()
            time.sleep(0.1)
        
run = FrontAppRPi()
run.periodic_update()
