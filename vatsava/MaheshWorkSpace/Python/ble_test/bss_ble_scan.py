from bluepy.btle import Scanner, DefaultDelegate

vehicle_id  = ""
kit_ble_adr = ""

# 
# class ScanDelegate(DefaultDelegate):
#     def __init__(self):
#         DefaultDelegate.__init__(self)
# 
#     def handleDiscovery(self, dev, isNewDev, isNewData):
#         if isNewDev:
#             print("Discovered device", dev.addr)
#         elif isNewData:
#             print( "Received new data from", dev.addr)

scanner = Scanner()
devices = scanner.scan(3.0)

for dev in devices:
#     print( "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
#         print ("  %s = %s" % (desc, value))
        if("Complete Local Name" == desc):
            vehicle_id = value
            kit_ble_adr = dev.addr
            
print("Vehicle ID   : ",vehicle_id)
print("Kit BLE Addr : ",kit_ble_adr)

