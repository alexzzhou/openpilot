import time
import cereal.messaging as messaging
import zmq

sm = messaging.SubMaster(['carState'])

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5556")

while True:
    sm.update(0)
    state = sm['carState']
    
    socket.send_string(str(state.vEgo))
    time.sleep(1)