import time
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")


socket.setsockopt_string(zmq.SUBSCRIBE, "")

# Process 5 updates

while True:
    string = socket.recv_string()
    print(string)
    time.sleep(1)
    
    


