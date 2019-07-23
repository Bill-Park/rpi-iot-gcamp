import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600)

sample_str = "[led on\r\n"
time.sleep(3)
ser.write(sample_str.encode())

ser.close()

