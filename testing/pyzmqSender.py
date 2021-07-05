import time
import cereal.messaging as messaging
from cereal import log
import zmq

sm = messaging.SubMaster(['carState'])

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.34.34.104:9000")


while True:
    sm.update()
    data = sm['carState']
    if data != None:
        print(type(data))
        socket.send(data.to_bytes())
    