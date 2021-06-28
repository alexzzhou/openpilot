import time
import cereal.messaging as messaging

sm = messaging.SubMaster(['sendcan', 'controlsState', 'carState','carControl', 'carEvents', 'carParams'])

while True:
    sm.update(0)
    state = sm['carState']
    print(state)
    time.sleep(1)