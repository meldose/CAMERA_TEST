import requests

pose_translation = []
'''
Write code to obtain pose from camera

while (5 sec)
    trigger camera
    response = getresponse
    pose_translation = getPose(response)
'''

pose_rotation = [] #check other codes to understand how orientation is found out

pose = pose_translation + pose_rotation


#joint angles = r.ik_fk("ik", pose )
#r.move_joint()


import os

from neurapy.camera.camera import Camera

class DummyCamera(Camera):
    def __init__(self, file_path='~/pose.txt'):
        self.file_path = os.path.expanduser(file_path)

    def read_pose_from_file(self) -> list:
        try:
            with open(self.file_path, 'r') as file:
                line = file.readline().strip()
                pose_data = [float(value) for value in line.split(',')]
                return pose_data
        except Exception as e:
            print(f"Failed to read pose from file: {e}")
            raise

    def get_pose(self) -> list:
        return self.read_pose_from_file()




######## for photoneo ##############

import CommunicationLibrary
import time
import json

CONTROLLER_IP="192.168.1.5"
PORT=11003

def test_ls():
    robot=CommunicationLibrary.RobotRequestResponseCommunication()
    robot.connect_to_server(CONTROLLER_IP,PORT)
    
    robot.pho_request_start_solution(252)
    robot.pho_request_ls_scan(1)
    robot.pho_ls_wait_for_scan()
    robot.pho_request_get_objects(1,5)
    time.sleep(2)
    robot.pho_request_ls_get_vision_system_status(1)
    time.sleep(1)
    robot.pho_request_ls_scan(1)
    robot.pho_ls_wait_for_scan()
    robot.pho_request_get_objects(1,1)
    time.sleeep(2)
    robot.pho_request_get_running_solution()
    time.sleep(30)
    robot.pho_request_get_available_solution()

    robot.close_request_get_available_solution()
    robot_close_connection()
    time.sleep(2)
