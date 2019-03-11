__author__ = "Brittain Cooke"

#imports
import sys
import RPi.GPIO as GPIO
import LiquidCrystalPi as lcrys
import time as time 
import datetime
import temp
import socket

#Varables and Declarations
option = 0 
threshold = 85
oldIP = '0.0.0.0'

#General GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Open log file
logs = open("/home/pi/Source/TempPi/Source/temp_logs.txt", "a")

#LCD setup
lcd = lcrys.LCD(15, 11, 22, 18, 16, 12)
lcd.begin(16,2)

#button
def buttonPress(channel):
    global option 
    option += 1
    if option >4:
        option =0

#logs
def writeLogs(t,h):
        dT = datetime.datetime.now()
        logs.write(dT.strftime("%Y-%m-%d %H:%M:%S | "))
        if t > -1 and h > -1:
            logs.write('Temp={0:0.1f}*F, Humidity={1:0.1f}%\n'.format(t,h))
        else:        
            logs.write('Failed to get reading.')

GPIO.setup(31, GPIO.IN, pull_up_down= GPIO.PUD_UP)
GPIO.add_event_detect(31, GPIO.FALLING, callback=buttonPress, bouncetime=1000)

#Main Loop
while True:
    t,h = temp.getAvgTemp()
    writeLogs(t,h)
    if option == 0:
    #Avg Temp Disp
        if t > -1 and h > -1:
            lcd.clear()
            lcd.write('AvgTemp={0:0.1f}*F'.format(t))
            lcd.nextline()
            lcd.write('Humidity={0:0.1f}%'.format(h))
            if t > threshold:
                temp.sendMsg()

    if option == 1:
        t,h = temp.getTemp(0)
        if t > -1 and h > -1:
            lcd.clear()
            lcd.write('1|Temp={0:0.1f}*F'.format(t))
            lcd.nextline()
            lcd.write('Humidity={0:0.1f}%'.format(h))

    if option == 2:
        t,h = temp.getTemp(1)
        if t > -1 and h > -1:
            lcd.clear()
            lcd.write('2|Temp={0:0.1f}*F'.format(t))
            lcd.nextline()
            lcd.write('Humidity={0:0.1f}%'.format(h))
            if t > threshold:
                temp.sendMsg()

    #IP Disp
    if option == 3:
        host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host.connect(('8.8.8.8',80))
        ip = host.getsockname()[0]
        if ip is not None and oldIP != ip:
            lcd.clear()
            lcd.write('IP:')
            lcd.nextline()
            lcd.write('{0}'.format(ip))
        else:
            lcd.write('Ip Error')
    #Config Disp
    if option == 4:
        lcd.clear()
        lcd.write('Configuration')


    if t > threshold:
        temp.sendMsg()

    time.sleep(.5)
