import serial.tools.list_ports
import serial

ports = list(serial.tools.list_ports.comports(include_links=False))
port = ""
ports_array = []
if len(ports) == 0:
    print("no com ports found")
    exit()
for p in ports:
        print(p)
        ports_array.append(p)
        port = str(p)[0:4]       

ser = serial.Serial(port,9600)

line = ""

while 1:
    if (ser.isOpen() == False): break
    try:
        inputChar = ser.read().decode("utf-8")
    except serial.serialutil.SerialException:
        print("lost serial connection")
        exit()
    
    if (inputChar != "\n"):
        line += inputChar
    else:
        #print(line)
        time = float(line[0:6])
        print("Time = "+str(time))
        line = ""





