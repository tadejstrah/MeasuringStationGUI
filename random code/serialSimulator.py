import serial
import serial.tools.list_ports
import time

ser = serial.Serial("COM1",9600)
ser2 = serial.Serial("COM2",9600)
while True:
    ser.write(str.encode("1 \t,2 \t, 3\t, 4 \t"))
    time.sleep(0.1)
    print(ser2.read())