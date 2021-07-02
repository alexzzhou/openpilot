import time
import cereal.messaging as messaging
import zmq

sm = messaging.SubMaster(['carState'])

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.34.34.26:9000")

while True:
    sm.update(0)
    state = sm['carState']
    print(state)
    socket.send_string(str(state.vEgo))
    time.sleep(1)