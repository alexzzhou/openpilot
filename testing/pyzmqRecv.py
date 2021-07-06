import time
import zmq
import signal

#exit handler function
def exit_handler():
    print("boo")

def main():

    # Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    current_ip = input("Current IP: ")
    socket.connect("tcp://"+current_ip+":9000")

    socket.setsockopt(zmq.SUBSCRIBE, b'')

    #data = socket.recv_json()
    #start_index = data["seq_number"]
    #start = time.perf_counter()
    cs_hist = []
    l_hist = []

    signal.signal(signal.SIGINT, exit_handler)

    while True:
        data = socket.recv_json()
        if data["type"] == "carState":
            cs_hist.append(data)
        
        elif data["type"] == "location":
            l_hist.append(data)

    
    #end = time.perf_counter()
    #print((end-start)/(5000-start_index))

if __name__ == "__main__":
    main()