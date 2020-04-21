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
        print(value)
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
    
chara = per.getDescriptors()
for i in range (len(chara)-1):
    print(chara[i])
    i+=1

desc = per.getDescriptors()
for i in range (len(desc)-1):
    print(desc[i])
    i+=1
    
# uuidValue = btle.UUID(0x2A38)
# heartSensorValue = heartService.getCharacteristics(uuidValue)[0]
# 
# val = heartSensorValue.read()
# print(binascii.b2a_hex(val))
# 
# uuidValue1 = btle.UUID(0x2A39)
# heartRate = heartService.getCharacteristics(uuidValue1)[0]
# 
# sai = """SSH into Raspberry Pi I generally log into my Raspberry Pi via SSH, or Secure Shell to give it its full name. This allows command line access, to your Raspberry Pi, from another computer. Although it is possible to SSH into the Raspberry Pi from anywhere in the world, and I do, this post only covers SSH access over the local network. I will cover remote connection in a future blog post.
# Although this"""
# #sri = bytes(sai,'utf-8')
# sri = (sai.encode())
# val1 = heartRate.write(sri)

# sai = "255"
# arr = bytes(sai, 'utf-8')
# per.writeCharacteristic(89,arr)
while(1):
    a = 1
#per.disconnect()