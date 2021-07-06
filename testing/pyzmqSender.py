import time
import cereal.messaging as messaging
from cereal import log
import zmq
import json

def to_json(data):
    dict = {

        "vEgo" : data.vEgo,         
        "aEgo" : data.aEgo,       
        "vEgoRaw" : data.vEgoRaw,     
        "yawRate" : data.yawRate,     
        "standstill" : data.standstill,
        "seq_number": 0

    }
    return dict

sm = messaging.SubMaster(['carState'])

context = zmq.Context()
socket = context.socket(zmq.PUB)
current_ip = input("Current IP: ")
socket.bind("tcp://"+current_ip+":9000")

current_num = 0
while True:
    sm.update(4)

    if sm.updated['carState']:
        msg = to_json(sm['carState'])
        current_num += 1
        msg["seq_number"] = current_num
        print(msg)
        socket.send_json(msg)