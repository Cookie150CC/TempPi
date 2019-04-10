# Class file for the Messenger Object type. Hold the functions for sending text alerts.
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

# Need to modify Email and password for use

import smtplib
from email.mime.text import MIMEText 

class Messenger():

    usr = "user@email.com"
    pwd = "secret"
    vtext = "@vtext.com"
    msg = "Temp is too high"

    def sendMsg(self,configObj):

        retval = 0 #Ok

        self.usr = configObj.emailAddress
        self.pwd = configObj.emailPassword
        if configObj.phoneCarrier == "verizon":
            self.vtext = configObj.phoneNumber + "@vtext.com"
        self.msg = "Temp is too high"

        mail = MIMEText("""From: %s
        To: %s
        Subject: txt alert
        Body: %s TEST""" % (self.usr,self.vtext,self.msg))

        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(self.usr,self.pwd)
            server.sendmail(self.usr,self.vtext,mail.as_string())
            server.quit()
        except:
            retval = 1 #error for failing to open server

        return retval
