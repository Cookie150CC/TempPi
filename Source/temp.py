import Adafruit_DHT as _dht
import smtplib
from email.mime.text import MIMEText 

#DHT setup
sensor0 = _dht.DHT22
sensor1 = _dht.DHT22
pins = [16, 12]

def getAvgTemp():
    h0, t0 = _dht.read_retry(sensor0, pins[0])
    h1, t1 = _dht.read_retry(sensor1, pins[1])
    if t0 is not None and h0 is not None and t1 is not None and h1 is not None:
        humidity = (h0+h1)/2
        temperature = (t0+t1)/2
        #For Farenheit vvvv Comment out for Celcius
        temperature = temperature * 9/5.0 + 32
    else:
        temperature = -1
        humidity = -1

    return temperature,humidity

def getTemp(sensor): 
    h0, t0 = _dht.read_retry(sensor0, pins[sensor])
    if t0 is not None and h0 is not None:
        t0 = t0 * 9/5.0 + 32
    else:
        t0 = -1
        h0 = -1

    return t0,h0


def sendMsg():
    usr = "user@gmail.com"
    pwd = "pwd"

    vtext = "5551235555@vtext.com"
    msg = "Temp is too high"

    mail = MIMEText("""From: %s
    To: %s
    Subject: txt alert
    Body: %s TEST""" % (usr,vtext,msg))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(usr,pwd)
    server.sendmail(usr,vtext,mail.as_string())
    server.quit()



