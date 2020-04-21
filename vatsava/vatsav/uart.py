import serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

while True:
    print ("hello")
    port.write(str.encode('\r\nSay something:'))
    rcv = port.read()
    port.write(str.encode('\r\nYou sent:'))
    port.write(str.encode(repr(rcv)))