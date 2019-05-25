import serial
#from serial.tools import list_ports

ser1 = serial.Serial('COM3')
ports = serial.tools.list_ports.comports()
print(ports)
ser1.close()

