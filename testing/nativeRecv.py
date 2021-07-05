import json
import zmq
import time 
import atexit

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:9000")

socket.setsockopt(zmq.SUBSCRIBE, b'')

time_list = []

start = time.perf_counter_ns()
time_list.append(start)

while True:
    data = socket.recv_json()
    time_list.append(time.perf_counter_ns())
    print(data)

    if data["seq_number"] >= 5000:
        break

for i in range(len(time_list), 1):
    time_list[i] = time_list[i] - time_list[i-1]    

time_list.pop(0)

print(sum(time_list)/len(time_list))