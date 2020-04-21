import time
import paho.mqtt.client as paho
import ssl

#define callbacks
def on_message(client, userdata, message):
  print("received message =",str(message.payload.decode("utf-8")))

def on_log(client, userdata, level, buf):
  print("log: ",buf)

def on_connect(client, userdata, flags, rc):
  with open("abhi_swap.json", "r") as jos:
      vats = jos.read
  print("publishing ")
  client.publish("sai","VAtsava",)

client=paho.Client() 
client.on_message=on_message
client.on_log=on_log
client.on_connect=on_connect
print("connecting to broker")
client.tls_set( ca_certs = "/home/pi/vatsav/testing/MQTT/certs/ca.pem",
                certfile = "/home/pi/vatsav/testing/MQTT/certs/01fda3c1b4-certificate.pem.crt",
                keyfile = "/home/pi/vatsav/testing/MQTT/certs/01fda3c1b4-private.pem.key",
                tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(False)
client.connect("a3hs4751kw4ggn.iot.ap-south-1.amazonaws.com", 8883, 60)

##start loop to process received messages

client.loop_start()
#wait to allow publish and logging and exit
time.sleep(1)
client.disconnect()
