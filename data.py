import random

def get_data():
	thermometer_value = random.randint(98,100)
	gauge_value = random.randint(1,100)
	graduatedbar_value = random.randint(1,100)
	leddisplay_value = random.randint(1,100)
	tank_value = random.randint(1,10)
	return thermometer_value, gauge_value, graduatedbar_value, leddisplay_value, tank_value