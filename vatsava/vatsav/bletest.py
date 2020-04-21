from bluepy.btle import *
from bluepy import btle
import time
import binascii

uid = "TS15UA1266"

scanner = Scanner()
devices = scanner.scan(3.0)

for dev in devices:
#print( "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():

        #print(desc)
#print ("  %s = %s" % (desc, value))
        if("Complete Local Name" == desc):
            if(uid == value):
                print(desc)
            else:
                print("vatsavaaaa")

print("connection initiated")
per = btle.Peripheral(dev.addr, "random")

print ("Services...")
for svc in per.services:
    print (svc)

heart = btle.UUID(0x180D)
heartService = per.getServiceByUUID(heart)
for ch in heartService.getCharacteristics():
    print (ch)

desc = per.getDescriptors()
for i in range (len(desc)-1):
    print(desc[i])
    i+=1
    
uuidValue = btle.UUID(0x2A38)
heartSensorValue = heartService.getCharacteristics(uuidValue)[0]

val = heartSensorValue.read()
print(binascii.b2a_hex(val))

uuidValue1 = btle.UUID(0x2A39)
heartRate = heartService.getCharacteristics(uuidValue1)[0]

sai = 0X34
#sri = bytes(sai,'utf-8')
val1 = heartRate.write(sai)

# sai = "255"
# arr = bytes(sai, 'utf-8')
# per.writeCharacteristic(89,arr)

per.disconnect()