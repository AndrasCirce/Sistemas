import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
gpio = 2
while True:
humidity.temperature = Adafruit_DHT.read_retry(sensor.gpio)
if humidity is not None and temperature is None:
	print('Temperatura = {0:0.1f}*C Humedad = {1:0.1f}%'.format(temperature, humidity))
else:
	break