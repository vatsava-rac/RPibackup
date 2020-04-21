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
        #print("available address are")
        print(dev.addr)
#print ("  %s = %s" % (desc, value))
        if("Complete Local Name" == desc):
            print("here1")
            if(uid == value):
                print("connection initiated")
                per = btle.Peripheral(dev.addr, "random")
                per.setSecurityLevel(level="high")
                print("addr is " + dev.addr)
                print(per.getState())

                print ("Services...")
                for svc in per.services:
                    print (svc)

                heart = btle.UUID(0x180F)
                heartService = per.getServiceByUUID(heart)
                for ch in heartService.getCharacteristics():
                    print (ch)

#                 desc = per.getDescriptors()
#                 for i in range (len(desc)-1):
#                     print(desc[i])
#                     i+=1
                    
                for desc in per.getDescriptors():
                    print(desc)
                    
                #uuidValue = btle.UUID(ec98aaf252fd11ea8d772e728ce88125)
                uuidValue = 'ec98aaf252fd11ea8d772e728ce88125'
                heartSensorValue = heartService.getCharacteristics(uuidValue)[0]
                print(heartSensorValue)

                val = heartSensorValue.read()
                print(binascii.b2a_hex(val))
                
                uuidValue1 = 'ec98aaf252fd11ea8d772e728ce88188'
                writechara = heartService.getCharacteristics(uuidValue1)[0]
                
                


                sai = """SSH into Raspberry Pi I generally log into my Raspberry Pi via SSH, or Secure Shell to give it its full name. This allows command line access, to your Raspberry Pi, from another computer. Although it is possible to SSH into the Raspberry Pi from anywhere in the world, and I do, this post only covers SSH access over the local network. I will cover remote connection in a future blog post.
                Although this"""
                sai1 = "I generally log into my"
                #sri = bytes(sai,'utf-8')
                sri = (sai.encode())
                sri1 = (sai1.encode())
                print(sri)
                val1 = writechara.write(sri)
                writechara.write(sri1)

                # sai = "255"
                # arr = bytes(sai, 'utf-8')
                # per.writeCharacteristic(89,arr)
                #while(1):
                    #a = 1
                time.sleep(5)
                per.disconnect()
            else:
                time.sleep(5)
                print("vatsavaaaa")
