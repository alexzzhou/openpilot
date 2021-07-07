import json
import zmq
import time 
import threading

class SenderThread(threading.Thread):

    def run(mystery, func):
        print("Starting Sender Thread.")
        print(mystery)
        func()
        

def senderThread():
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
        print(data)
        time.sleep(0.5)
        data["seq_number"] += 1

def main():
    #thread1 = threading.Thread(None, senderThread, 'Thread-1')
    #thread1.run()
    thread1 = SenderThread()
    thread1.start()

if __name__ == "__main__":
    main()