import time
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://10.34.34.104:9000")


while True:
    data = socket.recv_json()
    print(data)
    