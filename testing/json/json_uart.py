import json
import RPi.GPIO as GPIO

#UART = serial.Serial("/dev/ttyS0", 115200, timeout = 1)

people_string = '''
{
    "people" : [
        {
            "name" : "SAI",
            "age" : add
        },
        { 
            "name" : "VATSAVA",
            "age" : "24"
        }
    ]
}
'''
print(type(people_string))
with open("json.json", "a+") as jos:
    jos.write(people_string)