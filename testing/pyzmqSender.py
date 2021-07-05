import time
import cereal.messaging as messaging
from cereal import log
import zmq
import json

def to_json(data):
    dict = {
        "Velocitgy": data.vEgo,
        "Acceleration": data.aEgo,
        "Gas" : data.gas,
    }
    print(dict)
    return json.dumps(dict)

sm = messaging.SubMaster(['carState'])

context = zmq.Context()
socket = context.socket(zmq.PUB)
current_ip = input("Current IP: ")
socket.bind("tcp://"+current_ip+":9000")


while True:
    sm.update()
    data = sm['carState']
    socket.send_json(to_json(data))