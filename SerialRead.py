import serial
import time
import io

ser = serial.Serial('COM8', 9600, timeout=0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
s = ser.read(16)

while True:
    print(ser.read(100))
    time.sleep(3)
    sio.flush()
