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

#General GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Open log file
logs = open("temp_logs.txt", "a");

#LCD setup
lcd = lcrys.LCD(15, 11, 22, 18, 16, 12)
lcd.begin(16,2)

#button
def buttonPress(channel):
    global option 
    option += 1
    if option >2:
        option =0

GPIO.setup(31, GPIO.IN, pull_up_down= GPIO.PUD_UP)
GPIO.add_event_detect(31, GPIO.FALLING, callback=buttonPress, bouncetime=300)

#Main Loop
while True:
    if option == 0:
    #Temp Disp
        t,h = temp.getTemp()
        dT = datetime.datetime.now()
        logs.write(dT.strftime("%Y-%m-%d %H:%M:%S"))
        if t > -1 and h > -1:
            lcd.clear()
            logs.write('Temp={0:0.1f}*F, Humidity={0:0.1f}%\n'.format(t,h))
            lcd.write('Temp={0:0.1f}*F'.format(t))
            lcd.nextline()
            lcd.write('Humidity={0:0.1f}%'.format(h))
            if t > threshold:
                temp.sendMsg()
        else:
            logs.write('Failed to get reading.')
    #IP Disp
    if option == 1:
        host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host.connect(('8.8.8.8',80))
        ip = host.getsockname()[0]
        lcd.clear()
        if ip is not None:
            lcd.write('IP:')
            lcd.nextline()
            lcd.write('{0}'.format(ip))
        else:
            lcd.write('Ip Error')
    #Config Disp
    if option == 2:
        lcd.clear()
        lcd.write('Configuration')
    time.sleep(.5)
