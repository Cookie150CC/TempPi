# This is the file used to test the functions of python classes located in this folder.
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

import TSensor
import Messenger
import Config
import unittest

class TestTSensor(unittest.TestCase):

    def test_get_temp(self):#test for regular use case when correct sensor is provided
        
        tSensorObj = TSensor.TSensor()
        t0,h0 = tSensorObj.getTemp(0)
        t1,h1 = tSensorObj.getTemp(1)
        #print('Temp={0:0.1f}*F\n'.format(h))
        self.assertIsNotNone(t0, "Error with temp reading from TSensor 0. None returned as temp")
        self.assertIsNotNone(t1, "Error with temp reading from TSensor 1. None returned as temp")
        self.assertIsNotNone(h0, "Error with humidity reading from TSensor 0. None returned as humidity")
        self.assertIsNotNone(h1, "Error with humidity reading from TSensor 1. None returned as humidity")

    def test_get_avg_temp(self):#test for regular use cases

        tSensorObj = TSensor.TSensor()
        tAvg,hAvg = tSensorObj.getAvgTemp()
        self.assertIsNotNone(tAvg, "Error with temp reading from a sensor. None returned as Avg Temp")

class TestMessenger(unittest.TestCase):
    
    def test_send_msg(self):
        configObj = Config.Config()
        configObj.openJSON()
        messengerObj = Messenger.Messenger()
        tSensorObj = TSensor.TSensor()
        tAvg,hAvg = tSensorObj.getAvgTemp()
        retval = messengerObj.sendMsg(configObj,tAvg)
        self.assertEquals(retval,0,'Error sending message from sendMsg()')

if __name__ == '__main__':
        unittest.main()
