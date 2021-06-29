import cereal.messaging as messaging

sm = messaging.SubMaster(['carState'])
pm = messaging.PubMaster(['carVelo'])

while True:
    sm.update(0)
    state = sm['carState']
    pm.send('carVelo', state)
    time.sleep(1)
