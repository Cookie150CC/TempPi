# Class file for the TSensor object type. Used by the main.py file.
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

# The program is made to use DHT22 temperature sensors

#This Library is made by Adafruit under the MIT liscense. The code can be found at https://github.com/adafruit/Adafruit_Python_DHT
import Adafruit_DHT as _dht


class TSensor():
 
    #DHT setup
    sensor = _dht.DHT22
    pins = [16, 12]

    #Do temp reading of specified sensor
    def getTemp(self, pTSensor):
        h0, t0 = _dht.read_retry(self.sensor, self.pins[pTSensor])
        if t0 is not None and h0 is not None:
            t0 = t0 * 9/5.0 + 32

        return t0,h0

    #Get an average temp
    def getAvgTemp(self):
        
        h0, t0 = _dht.read_retry(self.sensor, self.pins[0])
        h1, t1 = _dht.read_retry(self.sensor, self.pins[1])
        if t0 is not None and h0 is not None and t1 is not None and h1 is not None:
            hAvg = (h0+h1)/2
            tAvg = (t0+t1)/2
            #For Farenheit vvvv Comment out for Celcius
            tAvg = tAvg * 9/5.0 + 32
        else:
            hAvg = None
            tAvg = None
        
        return tAvg, hAvg
