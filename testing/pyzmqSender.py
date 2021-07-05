import time
import cereal.messaging as messaging
from cereal import log
import zmq
import json

def to_json(data):
    dict = {
        "Velocity": data.vEgo,
        "Acceleration": data.aEgo,
        "Gas" : data.gas,
    }
    print(dict)
    return dict

sm = messaging.SubMaster(['carState'])

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.34.34.104:9000")


while True:
    sm.update()
    data = sm['carState']
    if data != None:
        socket.send_json(to_json(data))