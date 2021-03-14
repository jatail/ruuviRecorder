from influxdb import InfluxDBClient

def connectDB(influxCfg):
    dbClient = InfluxDBClient(host=influxCfg["host"], port=influxCfg["port"], username=influxCfg["username"], password=influxCfg["password"], database=influxCfg["db"], ssl=influxCfg["ssl"], verify_ssl=influxCfg["verify_ssl"])
    dbClient.create_database(influxCfg["db"])
    #print(dbClient.get_list_database())
    return dbClient

def writeToDB(dbClient, sensorList):
    for entry in sensorList:
        json_body = [
            {
                "measurement": "ruuvirecorder",
                "tags": {
                    "nickname": entry.nickname,
                    "mac": entry.mac
                },
                "fields": {
                    "temperature": entry.temperature,
                    "humidity": entry.humidity,
                    "pressure": entry.pressure,
                    "battery": entry.battery
                }
            }
        ]
        #print(json_body)
        dbClient.write_points(json_body)