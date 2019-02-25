import Adafruit_DHT as _dht
import smtplib
from email.mime.text import MIMEText 

#DHT setup
sensor0 = _dht.DHT22
sensor1 = _dht.DHT22
pin0 = 16
pin1 = 12

def getTemp():
    h0, t0 = _dht.read_retry(sensor0, pin0)
    h1, t1 = _dht.read_retry(sensor1, pin1)
    if t0 is not None and h0 is not None and t1 is not None and h1 is not None:
        humidity = (h0+h1)/2
        temperature = (t0+t1)/2
        #For Farenheit vvvv Comment out for Celcius
        temperature = temperature * 9/5.0 + 32
    else:
        temperature = -1
        humidity = -1

    return temperature,humidity


def sendMsg():
    usr = "cooke9619@gmail.com"
    pwd = "praise789"

    vtext = "2488401744@vtext.com"
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



