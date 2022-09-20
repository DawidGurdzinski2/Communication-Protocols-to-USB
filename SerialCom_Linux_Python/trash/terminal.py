import serial
import time


ser = serial.Serial('/dev/ttyACM0',115200)  # open serial port
print(ser.name)  

#x=ser.read()
#print(x)
#s=ser.read(10)
#print(s)
i=0
while(1):
    if(i==0):
        ser.write(b'e') 
        line=ser.readline()
        
        line=ser.readline()
        line=ser.readline()
        print(line)
    if(i==10):
        ser.write(b'g')
    if(i>=10):
        line=ser.readline()
        print(line)
    if(i==20):
        ser.write(b'e') 
    if(i==21):
        ser.write(b'e')     
    i=i+1
    print(i)
ser.close()   