import cereal.messaging as messaging

sm = messaging.SubMaster(['carState'])
pm = messaging.PubMaster(['carVelo'])

while True:
    sm.update(0)
    state = sm['carState'].vEgo
    pm.send('carVelo', bytes(state))
    time.sleep(1)
