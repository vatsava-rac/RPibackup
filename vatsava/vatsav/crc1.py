import time
import datetime
import RPi.GPIO as GPIO
import serial


##################################################################
# FUNCTION FOR THE XOR CALCULATION
#IT TAKES TWO PARAMETERS
def xor(a, b):

    result = []

    for i in range(1,len(b)):

        if a[i] == b[i]:
            result.append('0')

        else:
            result.append('1')

    return''.join(result)        


#DIVISION FOR THE DATA
def divi(divident, divisor):

    pick = len(divisor)
    temp = divident[0 : pick]

    while  pick < len(divident):
        
        if temp[0] == '1':
            temp = xor (divisor, temp)

        else:
            temp = xor('0'*pick, temp)

        pick = pick+1

    if temp[0] == '1':
        temp = xor(divisor , temp)
    else:
        temp = xor('0'*pick, temp)

    return temp
    
#DECODING THE DATA:
def decoding(data, key):

    a_key = len(key)

    appended_data = data + '0'*(a_key - 1)
    remainder = divi(appended_data, key)

    return remainder

UART = serial.Serial("/dev/ttyS0", 115200, timeout = 0.2)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

key = "1001"

##############################################################


while 1:
    
    b = UART.readline()
    data = b.decode()
    print(data)
    
    ans = decoding(data, key)

    if ans == '0':
        print("Data is correct")

    else:
        print("Data is wrong")        



