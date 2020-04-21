from bluepy.btle import Scanner, DefaultDelegate, UUID, Peripheral

usr_inpt    = "TS15UA1266"
vehicle_id   = ""
kit_ble_addr = ""

def scan_ble(str):
    scanner = Scanner()
    print("Scanning...")
    devices = scanner.scan(3.0)

    for dev in devices:
#print( "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
#print ("  %s = %s" % (desc, value))
            if("Complete Local Name" == desc):
                if(usr_inpt == value):
                    vehicle_id = value
                    return dev.addr
                else:
                    return 0    
            
kit_ble_addr = scan_ble (usr_inpt)
if (kit_ble_addr != 0):
    print("Vehicle ID   : ",usr_inpt)
    print("Kit BLE Addr : ",kit_ble_addr)

#Get kit service
    p = Peripheral(kit_ble_addr,"random")
    services=p.getServices()
#displays all services
    for service in services:
       print(service)
       print("")
    p.connect(kit_ble_addr)
    print("END")
    
else:
    print("Device not found")
    
# print("")
# print("Connecting to ",kit_ble_addr,"...")
# 

# 
