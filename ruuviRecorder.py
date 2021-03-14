import time
from rrDataHandler import SensorData, getData
from rrInflux import connectDB, writeToDB
from rrMqtt import connectMqtt, sendMqtt
from rrInit import loadNicknames, initialize

def main():
    cfg, nicknames = initialize()
    influxCfg = cfg["influx"]
    mqttCfg = cfg["mqtt"]
    if influxCfg["active"] == True:
        dbClient = connectDB(influxCfg)
    if mqttCfg["active"] == True:
        mqttClient = connectMqtt(mqttCfg)

    while(True):
        data = getData(nicknames)
        if influxCfg["active"] == True:
            writeToDB(dbClient, data)
        if mqttCfg["active"] == True:
            sendMqtt(mqttClient, mqttCfg["prefix"], data)
        time.sleep(cfg["ruuvirecorder"]["interval"])


if __name__ == "__main__":
    main()