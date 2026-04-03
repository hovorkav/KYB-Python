import paho.mqtt.client as mqtt
import threading

BROKER = "broker.hivemq.com"
PORT = 1883

topic = "mq-chat/spse/d32"

def conn(client, userdata, flags, rc, properties = None):
    print(f"Connected with result code {rc} on server "+topic)
def msg(client, userdata, msg):
    print(f"{msg.payload.decode()}")
#def sendmsg(client):
    
client = mqtt.Client()
client.on_connect = conn
client.on_message = msg
client.connect(BROKER, PORT, keepalive = 60)
client.subscribe(topic)

#username = "["+input("Nastav uzivatelske jmeno: ")+"]"
def inputLoop():
    zprava = input(">> ")
    client.publish(topic, zprava)
    
threading.Thread(target=inputLoop, daemon=True).start()

while True:
    client.loop()
    