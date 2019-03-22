# Main method for the directory. Project uses OOP.
# 2019 Brittain Cooke
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
_author__ = "Brittain Cooke"

#imports
import sys
import RPi.GPIO as GPIO
import LiquidCrystalPi as lcrys
import time as time 
import datetime
import socket

import TSensor
import Messenger
import Display

#Varables and declarations

tSensorObj = TSensor.TSensor()
messengerObj = Messenger.Messenger()
displayObj = Display.Display()
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
    if option >3:
        option =0

#logs
def writeLogs(t,h):
        dT = datetime.datetime.now()
        logs.write(dT.strftime("%Y-%m-%d %H:%M:%S | "))
        if t is not None and h is not None:
            logs.write('Temp={0:0.1f}*F, Humidity={1:0.1f}%\n'.format(t,h))
        else:        
            logs.write('Failed to get reading.')

GPIO.setup(31, GPIO.IN, pull_up_down= GPIO.PUD_UP)
GPIO.add_event_detect(31, GPIO.FALLING, callback=buttonPress, bouncetime=1000)

#Main Loop
while True:
    t,h = tSensorObj.getAvgTemp()
    writeLogs(t,h)
    if option == 0: #Avg Temp
        msg = [t,h]
        displayObj.doDisplayOptions(option,msg)
    elif option == 1: #Sensor 0 Temp
        t,h = tSensorObj.getTemp(0)
        msg = [t,h,0]
        displayObj.doDisplayOptions(option,msg)
    elif option == 2: #Sensor 1 Temp
        t,h = tSensorObj.getTemp(1)
        msg = [t,h,1]
        displayObj.doDisplayOptions(option,msg)
    elif option == 3: #IP
        msg = [oldIP]
        displayObj.doDisplayOptions(option,msg)

    if t > threshold:
        messengerObj.sendMsg()

    time.sleep(.5)
