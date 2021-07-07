import time
import cereal.messaging as messaging
from cereal import log
import zmq
import threading

class testThread(threading.Thread):
    
    def run():
        print("Starting " + self.name)

def format_cs(data):
    dict = {

        "vEgo" : data.vEgo,         
        "aEgo" : data.aEgo,       
        "vEgoRaw" : data.vEgoRaw,     
        "yawRate" : data.yawRate,     
        "standstill" : data.standstill,
        "seq_number": 0,
        "type" : "carState"

    }
    return dict

def senderThread():
    
    sm = messaging.SubMaster(['carState', 'liveLocationKalman'])

    context = zmq.Context()
    current_ip = input("Current IP: ")

    cs_socket = context.socket(zmq.PUB)
    cs_socket.bind("tcp://"+current_ip+":9000")

    l_socket = context.socket(zmq.PUB)
    l_socket.bind("tcp://"+current_ip+":9000")

    cs_seq = 0
    l_seq = 0

    while True:
        sm.update(5)
        
        if sm.updated['carState']:
            data = sm['carState']
            msg = format_cs(data)
            cs_seq += 1
            msg["seq_number"] = cs_seq
            print(msg)
            cs_socket.send_json(msg)

        if sm.updated['liveLocationKalman']:
            data = sm['liveLocationKalman']
            l_seq += 1
            msg = {
                "position" : (data.positionECEF.value[0], data.positionECEF.value[1], data.positionECEF.value[2]),
                "seq_number" : l_seq,
                "type" : "location"
            }

            print(msg)
            l_socket.send_json(msg)

def recvThread():
    context = zmq.Context()
    current_ip = input("Current IP: ")

    socket = context.socket(zmq.SUB)
    socket.connect("tcp://"+current_ip+":9001")

    socket.setsockopt(zmq.SUBSCRIBE, b'')

    data_hist = []

    while True:
        data = socket.recv_json()
        data_hist.append(data)     
    


def main():
    thread1 = threading.Thread(senderThread)
    thread2 = threading.Thread(recvThread)

    thread1.start()
    thread2.start()

if __name__ == "__main__":
    main()
