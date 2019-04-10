import json

class Config(): 
    threshold = 100
    phoneNumber = "5551234567"
    phoneCarrier = "carrier"
    emailAddress = "test@test.com"
    emailPassword = "secret"
    emailServer = "server.com"
    emailPort = 80
    logInterval = 10
    sendInterval = 15

    def openJSON(self):
        
        with open('/home/pi/Source/TempPi/Source/config.json') as jsonFile:
            jsonObj = json.load(jsonFile)
            obj = jsonObj['users'][0]
            self.threshold = int(obj['alert']['threshold'])
            self.phoneNumber = obj['phone']['number']
            self.phoneCarrier = obj['phone']['carrier']
            self.emailAddress = obj['email']['address']
            self.emailPassword = obj['email']['emailPassword']
            self.emailServer = obj['email']['server']
            self.emailPort = int(obj['email']['port'])
            self.logInterval = int(obj['logInterval'])
            self.sendInterval =int( obj['alert']['sendInterval'])
