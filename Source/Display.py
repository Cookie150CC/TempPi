# Class file for the Display object type. Used by the main.py file.
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


import socket

# This library vvvv is under the MIT Liscense this code can be found on github at https://github.com/graycatlabs/PyBBIO/tree/master/bbio/libraries/LiquidCrystal
import LiquidCrystalPi as lcrys

import sys
import RPi.GPIO as GPIO

#General GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Display():

    lcd = lcrys.LCD(15, 11, 22, 18, 16, 12)

    def displayAvgTemp(self,msg):
        if msg[0] is not None and msg[1] is not None:
            self.lcd.clear()
            self.lcd.write('AvgTemp={0:0.1f}*F'.format(msg[0]))
            self.lcd.nextline()
            self.lcd.write('Humidity={0:0.1f}%'.format(msg[1]))

    def displayTempSensor(self,msg):
        if msg[0] is not None and msg[1] is not None:
            self.lcd.clear()
            self.lcd.write('{0}|Temp={1:0.1f}*F'.format(msg[2],msg[0]))
            self.lcd.nextline()
            self.lcd.write('Humidity={0:0.1f}%'.format(msg[1]))

    def displayIP(self,msg):
        host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host.connect(('8.8.8.8',80))
        ip = host.getsockname()[0]
        if ip is not None and msg[0] != ip:
            self.lcd.clear()
            self.lcd.write('IP:')
            self.lcd.nextline()
            self.lcd.write('{0}'.format(ip))
        else:
            self.lcd.write('Ip Error')
    
    def doDisplayOptions(self, option, msg):
        self.lcd.begin(16,2)

        if option == 0:
            self.displayAvgTemp(msg)
        elif option == 1:
            self.displayTempSensor(msg)
        elif option == 2:
            self.displayTempSensor(msg)
        elif option == 3:
            self.displayIP(msg)


