#!/usr/bin/python
import serial

port = serial.Serial("/dev/ttyACM0", baudrate = 115200, timeout =1.0)
target = input("Target:")
target = target*4
commandNumber = str(84)
servoNum = input("Servo Number:")
servoNum = str(servoNum)
if len(servoNum) < 2:
    servoNum = ''.join(('0',servoNum))

print("ServoNum" +servoNum)
#turn target into bits
lowAndHigh ="{0:b}".format(target)
print(lowAndHigh)
print(len(lowAndHigh))

#While lowAndHigh is not a  14 bit binary number to split
while len(lowAndHigh)<14:
   lowAndHigh = ''.join(('0',lowAndHigh))

#Once I get it to a 14bit binary I can split it 
highTarget = lowAndHigh[:7]

lowTarget  = lowAndHigh[7:]
#Now that we have 2 bytes we need to get rid of most significant bit and replace it with 0
#highTarget = highTarget[1:]
highTarget = ''.join(('0',highTarget))
#lowTarget = lowTarget[1:]
lowTarget = ''.join(('0',lowTarget))
#Probibly not the most effecient 

#Now we can turn them into bytes

highTarget ='%X' % int(highTarget, 2)
lowTarget ='%X' % int(lowTarget, 2)
print(lowAndHigh)
 #Since hex 0F is shortened to F we need to add it back if this happens
if len(highTarget) != 2:
    highTarget = ''.join(('0',highTarget))

if len(lowTarget) != 2:
    lowTarget = ''.join(('0',lowTarget))

print('high '+highTarget)
print('low  '+lowTarget)  
print("servo: "+servoNum)

#command= ('\x' + commandNumber + '\x' + servoNum + '\x' + lowTarget + '\x' +highTarget) 
command = (commandNumber + servoNum + lowTarget + highTarget)
print(command)
command = command.decode("hex")
#test = command.decode("hex")

print(command)
port.write(command)