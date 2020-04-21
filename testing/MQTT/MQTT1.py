import paho.mqtt.publish as paho
from time import sleep
import os
import ssl

with open("abhi_idle.json", "r") as jos:
    a = jos.read()

paho.single("testing", a, hostname="test.mosquitto.org", protocol= paho.MQTTv311)