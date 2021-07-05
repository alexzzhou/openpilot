import time
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
current_ip = input("Current IP: ")
socket.connect("tcp://"+current_ip+":9000")

socket.setsockopt(zmq.SUBSCRIBE, b'')

while True:
    data = socket.recv_json()
    print(data)
    