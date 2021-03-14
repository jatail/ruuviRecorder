from ruuvitag_sensor.ruuvi import RuuviTagSensor

class SensorData:
    def __init__(self, mac, nickname, temperature, humidity, pressure, battery):
        self.mac = mac
        self.nickname = nickname
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.battery = battery

def getData(nicknames):
    sensorList = []
    datas = RuuviTagSensor.get_data_for_sensors()
    for key, val in datas.items():
        thisSensor = SensorData(key, "", float(val["temperature"]), float(val["humidity"]), float(val["pressure"]), float(val["battery"]))
        sensorList.append(thisSensor)
        if val["data_format"] == 3:
            thisSensor.battery = thisSensor.battery / 1000    
        thisSensor.nickname = nicknames.get(key)
        if thisSensor.nickname is None:
            thisSensor.nickname = thisSensor.mac
    return sensorList