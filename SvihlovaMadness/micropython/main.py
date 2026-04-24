import network
import umqtt.simple as mqtt
from time import sleep
#import LED

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("-//-", "...---...")

while not wifi.isconnected():
    print(".")
    sleep(1)
print(wifi.ifconfig())

def callback(topic, msg):
    print("Received message on topic {}: {}".format(topic, msg))
    #LED.blib()

client = mqtt.MQTTClient("hovorrrr", "192.168.1.1")
client.connect()
client.set_callback(callback)
client.publish("daniel", "Hi from Czechia")
client.subscribe("guy")
while True: 
    client.check_msg()
    sleep(1)