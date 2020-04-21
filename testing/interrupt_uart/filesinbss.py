# The data is continuously sent to raspberry pi from the MCU.
# Data is received when an interrupt is observed.
# Everything should be written in json format......

import RPi.GPIO as GPIO
import time
import datetime
import serial
import os
import csv
import json

d = {}
UART = serial.Serial("/dev/ttyS0", 115200, timeout = 1)
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(17,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

def UART_interrupt(channel):
    print("code is here")
    

    
    # Determining what the interrupt is for...
    uart_int = UART.readline()
    
    # Sending no.of stacks.
    if uart_int = "no_of_stacks":
        with open("stackscount.txt", "r") as stacks:
            no_of_stacks = stacks.read()

        no_of_stacks = int(no_of_stacks)
        print(type(no_of_stacks))
        print(no_of_stacks)
        
        UART.write(str.encode(no_of_stacks)) # Sending no of strings

    
    # Receiving the battery information from UART.
    elif uart_int = "batteries":   
        for i in range (no_of_stacks):
            b =  UART.readline()
            data = b.decode()
            data = "&0,0,0,0,0,0,0,0,0,0&2401,95,3009,0,55986,21760,12646,100,15875,1&2402,95,3009,0,55986,21760,12646,100,15875,1&2403,80,3009,0,55986,21760,12646,100,15875,1&2404,99,3009,0,55986,21760,12646,100,15875,1&2405,80,3009,0,55986,21760,12646,100,15875,1&0,0,0,0,0,0,0,0,0,0&0,0,0,0,0,0,0,0,0,0$B1[1][1],B1[2][1],B1[3][1],B1[4][1],B2[1][0],B2[2][0],B2[3][1],B2[4][0]"
            d["data{0}".format(i)] = data
            
        for i in range (no_of_stacks):   
            if len(d["data{0}".format(i)]) > 0:
                # stacks = stack_data(data)
                a, b = split_data (d["data{0}".format(i)])
                individual_batterty_data (a, i)
                latch_action(b)
        print("code is here also")
        
    else:
        print("INVALID INCOMING STRING.")

## Function to separate all the stacks separately 
#
# This function separares all the stacks separately. Information includes abiut the latch status and battery information.
# @note Delimiter used is "@".
# @returns Individual stack data in a list. 
# def stack_data (UART_data):
# 
#     incoming_data = UART_data.split("@")
#     return incoming_data

## Function to split the incoming data and log the details.
#
# This function splits the incoming data between batteries and latches.
# @note Delimiter used is "$".
# @returns Battery data and Latch data separately. 
def split_data (UART_data):
     
    #dividing the battery and latch data
    incoming_data = UART_data.split("$")
    batteries = incoming_data[0]
    latches = incoming_data[1]

    
    #battery data is stored in batterydata file
    with open("/home/pi/bss/log_data.txt", "a+") as logfile:
        a = datetime.datetime.now()
        logfile.write("%s" %a + " Data from BSS is received and is divided between battery and latch.\n")
    with open("/home/pi/bss/log_data.json", "a+") as logjson:
        a = datatime.datetime.now()
        "datareceived" : "%s" %a + " Data from BSS is received and is divided between battery and latch.\n"
        

    return batteries, latches

## Function for getting individual data
#
# Creates individual files for each battery pack and all the available battery packs present at the moment.
# Stores the information of the batteries which have in between 92 and 99 in thresCharge.txt
# @note Delimiter used to separate the battery data is "&". 

def individual_batterty_data(UART_data, stack_number):

    print("entering individual battery data")
    stack_number = str(stack_number)
    batteries = UART_data
    #separating the individual battery data
    battery = batteries.split("&")

    with open("/home/pi/bss/log_data.txt", "a+") as logfile:
        a = datetime.datetime.now()
        logfile.write("%s" %a  + " Battery data is separated.\n")

    with open("battereydata.txt", "a+") as datafile:
        a = datetime.datetime.now()
        datafile.write("%s" %a  + "%s\n" %batteries)

    # Storing the individual battery data in separate files.
    # Splitting the number of the batteries will be variable......
    # Ask surya to see if he can  send me the number of stacks available....

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
            
            
            
            #creating file for all the available batteries for each stack.
            battery_present_file = open("/home/pi/bss/battery_present.txt" ,"a+")
            battery_present_file.write(bat_j[0] + "\n")
            battery_present_file.close()

            with open("/home/pi/bss/stacks/stack"+stack_number+"/Stack" + stack_number + "BatList.txt", "a+") as stackBatteries:
                stackBatteries.write(bat_j[0] + " ")
                
            

            #creating separate file for batteries with Soc > 98
            #it checks for the available battery id's and write only if there is no id previously
            #creates the file soc.txt
            #soc_file = open("/home/pi/bss/soc.txt" ,"a+")
            #soc_file.close()
            bat_j[1] = int(bat_j[1])
            if bat_j[1] > 91 and bat_j[1] < 100:
                f = open("/home/pi/bss/thresCharge.txt", "a+")
                contents = f.read()
                f.close()
                if bat_j[0] in contents:
                    print("OK") 
                else:
                    soc_file = open("/home/pi/bss/thresCharge.txt" ,"a+")
                    soc_file.write("%s " %bat_j_id)
                    soc_file.close()
    
    # Trying to use a csv file here for available_Packs....              
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

    with open("/home/pi/bss/log_data.txt","a+") as logfile:
        a = datetime.datetime.now()
        logfile.write("%s" %a + " Separate files are created for each battery pack and data is stored.\n")
    
    soc_file = open("/home/pi/bss/soc.txt" ,"r")
    data = soc_file.read()
    soc_file.close()
    soc_file = open("/home/pi/bss/soc.txt" ,"a+")
    print(data.replace(missing," "))
#    if missing in data:
#        soc_file.write(data.replace("missing",""))
#         print("here")
#     else:
#         print("nothing")
    soc_file.close() 
    os.remove("/home/pi/bss/battery_present.txt")
    
    
## Function for checking the latch status
#
# Stores the values of latches in separate file latch_Data.
# Delimiter used here is ","
def latch_action(UART_data):
    
    #batteries, latches = split_data(UART_data)
    latches = UART_data
    latch = latches.split(",")

    #Latch data is stored in the file
    with open("latch_Data.txt", "a+") as latchfile:
        a = datetime.datetime.now()
        latchfile.write("%s" %a + " %s\n" %latches)    
    
    with open("/home/pi/bss/log_data.txt", "a+") as logfile:
        a = datetime.datetime.now()
        logfile.write("%s" %a + " Latch data is separated.\n")
    
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


GPIO.add_event_detect(23, GPIO.FALLING, callback=UART_interrupt)

while 1:
    

    
    #print("SAI SRI VATSAVA")
    #time.sleep(1)
    data = "&0,0,0,0,0,0,0,0,0,0&0,80,3009,0,55986,21760,12646,100,15875,1&2402,80,3009,0,55986,21760,12646,100,15875,1&2403,80,3009,0,55986,21760,12646,100,15875,1&2404,80,3009,0,55986,21760,12646,100,15875,1&2405,80,3009,0,55986,21760,12646,100,15875,1&0,0,0,0,0,0,0,0,0,0&0,0,0,0,0,0,0,0,0,0$B1[1][1],B1[2][1],B1[3][1],B1[4][1],B2[1][0],B2[2][0],B2[3][1],B2[4][0]"
#     b =  UART.readline()
#     data = b.decode()
#     if len(data) > 0:
#         stacks = stack_data(data)
#         for i in range (0, len(stacks)):
#             a, b = split_data (stacks[i])
#             individual_batterty_data (a, i)
#             latch_action(b)


    # GPIO.output(17,GPIO.HIGH)
    # b = datetime.datetime.now()
    # time.sleep(0.5)    
    # logfile = open("/home/pi/bss/log.txt","a+")
    # logfile.write("%s" %b)
    # logfile.write("LED 1 IS ON\n")
    # logfile.close()
    # GPIO.output(17,GPIO.LOW)
    # time.sleep(0.5)
    # b = datetime.datetime.now()
    # logfile = open("/home/pi/bss/log.txt","a+")    
    # logfile.write("%s" %b)
    # logfile.write("LED 1 IS OFF\n")
    # logfile.close()    