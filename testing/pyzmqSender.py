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
current_ip = input("Current IP: ")

cs_socket = context.socket(zmq.PUB)
cs_socket.bind("tcp://"+current_ip+":9000")

l_socket = context.socket(zmq.PUB)
l_socket.bind("tcp://"+current_ip+":9001")

cs_seq = 0
l_seq = 0

while True:
    sm.update(10)
    
    """
    if sm.updated['carState']:
        data = sm['carState']
        msg = format_cs(data)
        cs_seq += 1
        msg["seq_number"] = cs_seq
        print(msg)
        cs_socket.send_json(msg)
    """

    if sm.updated['liveLocationKalman']:
        data = sm['liveLocationKalman']
        l_seq += 1
        msg = {
            "position" : data.positionECEF.value,
            "seq_number" : l_seq
        }
        print(msg)
        cs_socket.send_json(msg)