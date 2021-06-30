import time
import cereal.messaging as messaging

sm = messaging.SubMaster(['carState'])
pm = messaging.PubMaster(['carVelo'])

while True:
    sm.update(0)
    state = sm['carState']
    msg = messaging.new_message('carVelo')
    msg.carVelo = state
    print(msg)
    pm.send('carVelo', msg)
    time.sleep(1)
