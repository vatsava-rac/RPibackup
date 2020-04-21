import RPi.GPIO as GPIO
import time
import datetime
import serial

UART = serial.Serial("/dev/ttyS0", 115200, timeout = 1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

while 1:
    
    #b =  UART.readline()
    #data = b.decode()
    data = "#2400,80,3009,0,55986,21760,12646,100,15875,1#2401,80,3009,0,55986,21760,12646,100,15875,1#2402,80,3009,0,55986,21760,12646,100,15875,1#2403,80,3009,0,55986,21760,12646,100,15875,1#2404,80,3009,0,55986,21760,12646,100,15875,1#2405,80,3009,0,55986,21760,12646,100,15875,1#0,0,0,0,0,0,0,0,0,0#0,0,0,0,0,0,0,0,0,0$b1,b2,b3,b4,b5,b6,b7,b8"
    print(data)

    if len(data) > 0:
        print(data)

        #incoming data is logged to log file        
        a = datetime.datetime.now()
        logfile = open("log.txt","a+")
        logfile.write("%s" %a)
        logfile.write("  data is received\n")
        logfile.close()
        
        #dividing the battery and latch data
        incoming_data = data.split("$")
        batteries = incoming_data[0]
        latches = incoming_data[1]
        print(batteries)
        
        
        #separating the individual battery data
        
        battery = batteries.split("&")
        battery_1 = battery[1]
        battery_2 = battery[2]
        battery_3 = battery[3]
        battery_4 = battery[4]
        battery_5 = battery[5]
        battery_6 = battery[6]
        battery_7 = battery[7]
        battery_8 = battery[8]
        
        a = datetime.datetime.now()
        logfile = open("log.txt","a+")
        logfile.write("%s" %a)
        logfile.write("  data is divided between battery and latch\n")
        logfile.close()        
        
        
        a = datetime.datetime.now()
        logfile = open("log.txt","a+")
        logfile.write("%s" %a)
        logfile.write("  battery data is separeted\n")
        logfile.close()        
        
        #separating the imdividual latch data
        latch = latches.split(",")
        latch_1 = latches[0]
        latch_2 = latches[1]
        latch_3 = latches[2]
        latch_4 = latches[3]
        latch_5 = latches[4]
        latch_6 = latches[5]
        latch_7 = latches[6]
        latch_8 = latches[7]
        
        bat1 = battery_1.split(",", 1)
        bat1_id = bat1[0]
        if len(bat1_id) > 1:
            a = datetime.datetime.now()
            k = bat1_id + ".txt"
            bat1file = open(k,"a+")
            bat1file.write("%s" %a)
            bat1file.write("  %s" %battery_1)
            bat1file.write("\n")
            bat1file.close()
            
        bat2 = battery_2.split(",", 1)
        bat2_id = bat2[0]
        if len(bat2_id) > 1:
            a = datetime.datetime.now()
            k = bat2_id + ".txt"
            bat2file = open(k,"a+")
            bat2file.write("%s" %a)
            bat2file.write("  %s" %battery_2)
            bat2file.write("\n")
            bat2file.close()            
            
        bat3 = battery_3.split(",", 1)
        bat3_id = bat3[0]
        if len(bat3_id) > 1:
            a = datetime.datetime.now()
            k = bat3_id + ".txt"
            bat3file = open(k,"a+")
            bat3file.write("%s" %a)
            bat3file.write(" %s" %battery_3)
            bat3file.write("\n")
            bat3file.close()
            
        bat4 = battery_4.split(",", 1)
        bat4_id = bat4[0]
        if len(bat4_id) > 1:
            a = datetime.datetime.now()
            k = bat4_id + ".txt"
            bat4file = open(k,"a+")
            bat4file.write("%s" %a)
            bat4file.write(" %s" %battery_4)
            bat4file.write("\n")
            bat4file.close()
            
        bat5 = battery_5.split(",", 1)
        bat5_id = bat5[0]
        if len(bat5_id) > 1:
            a = datetime.datetime.now()
            k = bat5_id + ".txt"
            bat5file = open(k,"a+")
            bat5file.write("%s" %a)
            bat5file.write(" %s" %battery_5)
            bat5file.write("\n")
            bat5file.close()
            
        bat6 = battery_6.split(",", 1)
        bat6_id = bat6[0]
        if len(bat6_id) > 1:
            a = datetime.datetime.now()
            k = bat6_id + ".txt"
            bat6file = open(k,"a+")
            bat6file.write("%s" %a)
            bat6file.write(" %s" %battery_6)
            bat6file.write("\n")
            bat6file.close()
            
        bat7 = battery_7.split(",", 1)
        bat7_id = bat7[0]
        if len(bat7_id) > 1:
            a = datetime.datetime.now()
            k = bat7_id + ".txt"
            bat7file = open(k,"a+")
            bat7file.write("%s" %a)
            bat7file.write(" %s" %battery_7)
            bat7file.write("\n")
            bat7file.close()
            
        bat8 = battery_8.split(",", 1)
        bat8_id = bat8[0]
        if len(bat8_id) > 1:
            a = datetime.datetime.now()
            k = bat8_id + ".txt"
            bat8file = open(k,"a+")
            bat8file.write("%s" %a)
            bat8file.write(" %s" %battery_8)
            bat8file.write("\n")
            bat8file.close()            

        #Latch data is stored in the file
        a = datetime.datetime.now()
        logfile = open("log.txt","a+")
        logfile.write("%s" %a)
        logfile.write("  latch data is separeted\n")
        logfile.close()
        
        dataFile = open("latchdata.txt","a+")
        dataFile.write('%s' %a)    
        dataFile.write("  %s\n" %latches)
        dataFile.close()
        
        #All batteries data is stored.
        dataFile = open("data.txt","a+")
        dataFile.write('%s' %a)    
        dataFile.write("  %s\n" %batteries)
        dataFile.close()
        
        first = str.encode('B1\r\n')
        second = str.encode('B2\r\n')

        if (data == first):
            UART.write(str.encode('UNLOCK_B1\n'))
            
        elif (data == second):
            UART.write(str.encode('UNLOCK_B2\n'))
            
        a = datetime.datetime.now()
        logfile = open("log.txt","a+")
        logfile.write("%s" %a)
        logfile.write("  data is stored in log\n")
        logfile.close()
        time.sleep(0.5)
    
    GPIO.output(17,GPIO.HIGH)
    b = datetime.datetime.now()
    time.sleep(0.5)    
    logfile = open("log.txt","a+")
    logfile.write("%s" %b)
    logfile.write("LED 1 IS ON\n")
    logfile.close()
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    b = datetime.datetime.now()
    logfile = open("log.txt","a+")    
    logfile.write("%s" %b)
    logfile.write("LED 1 IS OFF\n")
    logfile.close()
    


    