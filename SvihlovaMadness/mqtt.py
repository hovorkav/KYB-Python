import paho.mqtt.client as mq

BROKER = "broker.hivemq.com"
PORT = 1883

topic = "test/topic"

def conn(client, userdata, flags, rc, properties = None):
    print(f"Connected with result code {rc}")
def msg(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mq.Client()
client.on_connect = conn
client.on_message = msg
client.connect(BROKER, PORT, keepalive = 60)
client.subscribe(topic)

while True:
    client.loop()
    #msg = input("Hlas do sveta: ")
    #client.publish(topic, msg)

#client.loop_forever()