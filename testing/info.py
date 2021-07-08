import time
import cereal.messaging as messaging

sm = messaging.SubMaster(['sendcan', 'controlsState', 'carState','carControl', 'carEvents', 'carParams', 'driverCameraState'])

while True:
    sm.update(0)
    if sm.updated['driverCameraState']:
        state = sm['driverCameraState']
        print(state)
        time.sleep(1)