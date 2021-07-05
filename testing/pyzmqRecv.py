import time
import zmq
import capnp
from cereal import log

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://10.34.34.104:9000")


socket.setsockopt(zmq.SUBSCRIBE, "")


while True:
    data = socket.recv()
    