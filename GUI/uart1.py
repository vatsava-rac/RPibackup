#!/usr/bin/env python        
import time
import serial
import datetime

               
UART = serial.Serial("/dev/ttyS0", 115200)

str1 = ""

def main():


    b =  UART.readline()
    data = b.decode()

    time = datetime.datetime.now()
    logfile = open("/home/pi/BSS/swap_log/log.txt","a+")
    logfile.write("%s" %time)
    logfile.write("  data is received\n")
    logfile.close()

    dataFile = open("/home/pi/BSS/swap_log/data.txt","a+")
    dataFile.write('%s' %time)    
    dataFile.write("  %s\n" %data)
    dataFile.close()
    
    str1 = "B1"
    str2 = "B2"
    print(str1)
    
    if data == str1:
        UART.write(str.encode('UNLOCKB1\r\n'))
    elif data == str2:
        var = 2
        UART.write(str.encode('UNLOCKB2\r\n'))

    time = datetime.datetime.now()
    logfile = open("/home/pi/BSS/swap_log/log.txt","a+")
    logfile.write("%s" %time)
    logfile.write("  data is stored in log\n")
    logfile.close()    


    UART.write(str.encode('Sent OK\r\n'))

        

if __name__=="__main__":
    main()



        