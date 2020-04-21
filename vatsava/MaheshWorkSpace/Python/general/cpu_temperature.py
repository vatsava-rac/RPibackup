#from gpiozero import CPUTemperature
import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time                              # calling for time to provide delays in program
IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
IO.setwarnings(False)
IO.setup(37,IO.OUT)             # initialize digital pin40 as an output.
IO.output(37,1)                      # turn the LED on (making the voltage level HIGH)

#cpu = CPUTemperature()

#print(cpu.temperature)
