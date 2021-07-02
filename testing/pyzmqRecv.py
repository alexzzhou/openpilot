import time
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.0.100:9000")


socket.setsockopt_string(zmq.SUBSCRIBE, "")


while True:
    string = socket.recv_string()
    print(string)
    time.sleep(1)