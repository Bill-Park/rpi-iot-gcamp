import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True :
	r = ser.read()
	print(r)

ser.close()
