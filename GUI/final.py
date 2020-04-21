import RPi.GPIO as GPIO
import time
import datetime
import serial
import os

UART = serial.Serial("/dev/ttyS0", 115200, timeout = 1)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

#Function to split the incoming data and log the details
def split_data (UART_data):
           
    a = datetime.datetime.now()
    logfile = open("/home/pi/bss/log.txt","a+")
    logfile.write("%s" %a)
    logfile.write("  data is received\n")
    logfile.close()
        
    #dividing the battery and latch data
    incoming_data = UART_data.split("$")
    batteries = incoming_data[0]
    latches = incoming_data[1]
    #print(incoming_data)
    
    #battery data is stored in batterydata file
    a = datetime.datetime.now()
    logfile = open("/home/pi/bss/log.txt","a+")
    logfile.write("%s" %a)
    logfile.write("  data is divided between battery and latch\n")
    logfile.close()
        
    return batteries, latches

#Function for getting individual data
#Creates individual files for each battery pack.
#Stores the information of the batteries which have Soc > 98 in soc.txt
def individual_batterty_data(UART_data):
    
    batteries, latches = split_data(UART_data)
    
    #separating the individual battery data
    battery = batteries.split("&")
    a = datetime.datetime.now()
    logfile = open("/home/pi/bss/log.txt","a+")
    logfile.write("%s" %a)
    logfile.write("  battery data is separeted\n")
    logfile.close()
    
    a = datetime.datetime.now()
    datafile = open("batterydata.txt","a+")
    datafile.write("%s" %a)
    datafile.write(" %s\n" %batteries)
    datafile.close()
    
    #Storing the individual battery data in separate files.
    for j in range (1, 9):
        bat_j = battery[j].split(",")
        bat_j_id = bat_j[0]
        if len(bat_j_id) > 2:
            a = datetime.datetime.now()
            k = bat_j_id + ".txt"
            bat_j_file = open("/home/pi/bss/batterydata/" + k, "a+")
            bat_j_file.write("%s" %a)
            bat_j_file.write("%s" %battery[j])
            bat_j_file.write("\n")
            bat_j_file.close()
            
            #creating file for all the available batteries.
            battery_present_file = open("/home/pi/bss/battery_present.txt" ,"a+")
            #battery_present_file = open("/home/pi/bss/battery_present.txt" ,"a+")
            battery_present_file.write(bat_j[0] + " ")
            battery_present_file.close()
            
            #creating separate file for batteries with Soc > 98
            #it checks for the available battery id's and write only if there is no id previously
            #creates the file soc.txt
            soc_file = open("/home/pi/bss/soc.txt" ,"a+")
            soc_file.close()
            if bat_j[1] == "80" or bat_j[1] == "99" or bat_j[1] == "100":
                f = open("/home/pi/bss/soc.txt", "r")
                contents = f.read()
                f.close()
                if bat_j[0] in contents:
                    print("OK") 
                else:
                    soc_file = open("/home/pi/bss/soc.txt" ,"a+")
                    soc_file.write("%s " %bat_j_id)
                    soc_file.close()
                    print("it is here")
                    
    battery_present_file = open("/home/pi/bss/battery_present.txt", "r")
    battery_present = battery_present_file.read()
    battery_present_file.close()
    li1 = list(battery_present.split(" "))
    
    soc_file = open("/home/pi/bss/soc.txt" ,"r")
    soc_data = soc_file.read()
    soc_file.close()
    li2 = list(soc_data.split(" "))
    
    missing_value = set(li2).difference(li1)
    print(li1)
    print(li2)
    
    miss = str(missing_value)
    print(len(miss))
    missing = ''
    missing = miss.replace("{'", "")
    missing = missing.replace("'}","")

    print(missing)
    a = datetime.datetime.now()
    logfile = open("/home/pi/bss/log.txt","a+")
    logfile.write("%s" %a)
    logfile.write("  separate files are created for each battery pack and data is stored.\n")
    logfile.close()
    
    soc_file = open("/home/pi/bss/soc.txt" ,"r")
    data = soc_file.read()
    soc_file.close()
    soc_file = open("/home/pi/bss/soc.txt" ,"a+")
    print(data.replace(missing," "))
#     if missing in data:
#         soc_file.write(data.replace("missing",""))
#         print("here")
#     else:
#         print("nothing")
    soc_file.close() 
    os.remove("/home/pi/bss/battery_present.txt")
    
    
#function for checking the latch status
#stores the values of latches in separate file latchdata
def latch_action(UART_data):
    
    batteries, latches = split_data(UART_data)
    latch = latches.split(",")

    #Latch data is stored in the file
    a = datetime.datetime.now()
    dataFile = open("latchdata.txt","a+")
    dataFile.write('%s' %a)    
    dataFile.write("  %s\n" %latches)
    dataFile.close()    
    
    a = datetime.datetime.now()
    logfile = open("/home/pi/bss/log.txt","a+")
    logfile.write("%s" %a)
    logfile.write("  latch data is separeted\n")
    logfile.close()
    
    if latch[0][6] + latch[1][6] + latch[2][6] + latch[3][6] == "1111":
        print("BOX 1 IS OPEN")
    elif latch[0][6] + latch[1][6] + latch[2][6] + latch[3][6] == "0000":
        print("BOX 1 IS CLOSED")
    else:
        print("ERROR 1")
        
    if latch[4][6] + latch[5][6] + latch[6][6] + latch[7][6] == "1111":
        print("BOX 2 IS OPEN")
    elif latch[4][6] + latch[5][6] + latch[6][6] + latch[7][6] == "0000":
        print("BOX 2 IS CLOSED")
    else:
        print("ERROR 2")    
                

while 1:
    
    #b =  UART.readline()
    #data = b.decode()
    data = "&0,0,0,0,0,0,0,0,0,0&0,80,3009,0,55986,21760,12646,100,15875,1&2402,80,3009,0,55986,21760,12646,100,15875,1&2403,80,3009,0,55986,21760,12646,100,15875,1&2404,80,3009,0,55986,21760,12646,100,15875,1&2405,80,3009,0,55986,21760,12646,100,15875,1&0,0,0,0,0,0,0,0,0,0&0,0,0,0,0,0,0,0,0,0$B1[1][1],B1[2][1],B1[3][1],B1[4][1],B2[1][0],B2[2][0],B2[3][1],B2[4][0]"
    
    if len(data) > 0:
        a, b = split_data (data)
        individual_batterty_data (data)
        latch_action(data)

    GPIO.output(17,GPIO.HIGH)
    b = datetime.datetime.now()
    time.sleep(0.5)    
    logfile = open("/home/pi/bss/log.txt","a+")
    logfile.write("%s" %b)
    logfile.write("LED 1 IS ON\n")
    logfile.close()
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    b = datetime.datetime.now()
    logfile = open("/home/pi/bss/log.txt","a+")    
    logfile.write("%s" %b)
    logfile.write("LED 1 IS OFF\n")
    logfile.close()    