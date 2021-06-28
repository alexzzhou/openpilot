import cereal.messaging as messaging

sm = messaging.SubMaster(['carState'], addr = "192.168.0.100")

while True:
    sm.update(0)
    state = sm['carState']
    print(state)
    time.sleep(1)