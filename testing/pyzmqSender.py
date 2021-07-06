import time
import cereal.messaging as messaging
from cereal import log
import zmq
import json

def format_cs(data):
    dict = {

        "vEgo" : data.vEgo,         
        "aEgo" : data.aEgo,       
        "vEgoRaw" : data.vEgoRaw,     
        "yawRate" : data.yawRate,     
        "standstill" : data.standstill,
        "seq_number": 0

    }
    return dict

sm = messaging.SubMaster(['carState', 'liveLocationKalman'])

context = zmq.Context()

cs_socket = context.socket(zmq.PUB)
current_ip = input("Current IP: ")
cs_socket.bind("tcp://"+current_ip+":9000")

l_socket = context.socket(zmq.PUB)
current_ip = input("Current IP: ")
l_socket.bind("tcp://"+current_ip+":9001")

current_num = 0
while True:
    sm.update(10)

    if sm.updated['carState']:
        data = sm['carState']
        msg = format_cs(data)
        current_num += 1
        msg["seq_number"] = current_num
        print(msg)
        cs_socket.send_json(msg)

    if sm.updated['liveLocationKalman']:
        data = sm['liveLocationKalman']
        msg = to_json(data)
        current_num += 1
        msg["seq_number"] = current_num
        print(msg)
        cs_socket.send_json(msg)