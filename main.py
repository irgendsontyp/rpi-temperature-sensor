import re
import time

try:
	while (True):
		with open("/sys/bus/w1/devices/28-0416c5235eff/w1_slave") as f:
			fullString = f.read()

			if (re.search("crc=\w+ YES", fullString)):
				temperatureStringMatch = re.search("t=(\d+)", fullString)
				
				print (str(round(float(temperatureStringMatch.group(1)) / 1000)) + "°C")
					
		time.sleep(5)
except KeyboardInterrupt:
	print("Good bye!")
