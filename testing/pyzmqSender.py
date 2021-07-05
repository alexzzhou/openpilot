import time
import cereal.messaging as messaging
from cereal import log
import zmq

sock = messaging.sub_sock('carState')

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.34.34.104:9000")


while True:
    data = messaging.recv_one_or_none(sock)
    if data != None:
        print(data)
        socket.send_string(str(data.vEgo))
    