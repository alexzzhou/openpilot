import json
import zmq
import time 

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:9000")

    data = {
        "banana" : 5,
        "apple" : 2,
        "seq_number": 0
    }

    json_data = json.dumps(data)

    while True:
        socket.send_json(data)
        time.sleep(0.01)
        data["seq_number"] += 1

if __name__ == "__main__":
    main()