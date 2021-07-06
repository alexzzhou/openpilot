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
    sm.update(10)
    print(sm['carState'])
    if sm.updated['carState']:
        data = sm['carState']
        msg = to_json(data)
        current_num += 1
        msg["seq_number"] = current_num
        #print(msg)
        socket.send_json(msg)