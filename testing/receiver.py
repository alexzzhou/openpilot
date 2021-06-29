import time
import cereal.messaging as messaging

sm = messaging.SubMaster(['carVelo'])

while True:
    sm.update(0)
    state = sm['carVelo'].vEgo
    print(state)
    time.sleep(1)