import time
import datetime
import serial

def Convert(string):
    battery_1 = list(string.split(","))
    return battery_1
                     
str1 = "2400,43,2340,14,7204,934,277,98,647,0"
a = Convert(str1)
print(a[0])


dataFile = open(a[0],"a+")    
dataFile.write("  %s\n" %str1)
dataFile.close()



        

    


    
