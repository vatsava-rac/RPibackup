import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
import json
import logging

logging.basicConfig(level=logging.INFO)

class PubSub(object):

    def __init__(self, listener = False, topic = "default"):
        self.connect = False
        self.listener = listener
        self.topic = topic
        self.logger = logging.getLogger(repr(self))

    def __on_connect(self, client, userdata, flags, rc):
        self.connect = True
        
        if self.listener:
            self.mqttc.subscribe(self.topic)

        self.logger.debug("{0}".format(rc))

    def __on_message(self, client, userdata, msg):
        self.logger.info("{0}, {1} - {2}".format(userdata, msg.topic, msg.payload))

    def __on_log(self, client, userdata, level, buf):
        self.logger.debug("{0}, {1}, {2}, {3}".format(client, userdata, level, buf))

    def bootstrap_mqtt(self):

        self.mqttc = paho.Client()
        self.mqttc.on_connect = self.__on_connect
        self.mqttc.on_message = self.__on_message
        self.mqttc.on_log = self.__on_log

        awshost = "5.196.95.208" # host name
        awsport = 8884

        caPath = "/home/pi/vatsav/testing/MQTT/mos_certs/mosquitto.org.crt" #ca certificate
        certPath = "/home/pi/vatsav/testing/MQTT/mos_certs/client.crt" # device publick key
        keyPath = "/home/pi/vatsav/testing/MQTT/mos_certs/client.key" # device private key 

        self.mqttc.tls_set(caPath, 
            certfile=certPath, 
            keyfile=keyPath, 
            cert_reqs=ssl.CERT_REQUIRED, 
            tls_version=ssl.PROTOCOL_TLSv1_2, 
            ciphers=None)

        result_of_connection = self.mqttc.connect(awshost, awsport, keepalive=120)

        if result_of_connection == 0:
            self.connect = True

        return self

    def start(self):
        self.mqttc.loop_start()

        while True:
            sleep(2)
            if self.connect == True:
                with open("abhi_swap.json", "r") as jos:
                    a = jos.read()
                
                self.mqttc.publish(self.topic, a, qos=1)
            else:
                self.logger.debug("Attempting to connect.")

if __name__ == '__main__':
   
    PubSub(listener = True, topic = "iot").bootstrap_mqtt().start() #publish topic