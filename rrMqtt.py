import paho.mqtt.client as mqtt

def connectMqtt(mqttCfg):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client(client_id=mqttCfg["client_id"])
    client.on_connect = on_connect
    client.connect(mqttCfg["host"], mqttCfg["port"])
    return client

def sendMqtt(mqttClient, prefix, sensorList):
    for entry in sensorList:
        mqttClient.publish(prefix+"/"+entry.nickname.lower()+"/temperature", entry.temperature)
        mqttClient.publish(prefix+"/"+entry.nickname.lower()+"/humidity", entry.humidity)
        mqttClient.publish(prefix+"/"+entry.nickname.lower()+"/pressure", entry.pressure)
        mqttClient.publish(prefix+"/"+entry.nickname.lower()+"/battery", entry.battery)