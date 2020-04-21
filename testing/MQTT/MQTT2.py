import paho.mqtt.publish as mqtt
#import paho.mqtt.client
from time import sleep
import os
import ssl

with open("/home/pi/vatsav/testing/MQTT/abhi_idle.json", "r") as jos:
    a = jos.read()

b = {
        "ca_certs": "/home/pi/vatsav/testing/MQTT/mqttcerts/mqtt_ca.crt",
        "certfile":"/home/pi/vatsav/testing/MQTT/mqttcerts/mqtt_client.crt",
        "keyfile":"/home/pi/vatsav/testing/MQTT/mqttcerts/mqtt_client.key",
        "tls_version":ssl.PROTOCOL_TLSv1_2, "ciphers":None
       }

mqtt.single("iot/bss/telemetry", payload = a, hostname="http://ec2-13-235-90-136.ap-south-1.compute.amazonaws.com/",tls = b,
             transport="tcp")
