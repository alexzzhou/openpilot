import time
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
current_ip = input("Current IP: ")
socket.connect("tcp://"+current_ip+":9000")

socket.setsockopt(zmq.SUBSCRIBE, b'')

data = socket.recv_json()
start_index = data["seq_number"]
start = time.perf_counter()

while True:
    data = socket.recv_json()
    print(data)
    if data["seq_number"] >= 50:
        break

end = time.perf_counter()

print((end-start)/(50-start_index))