#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
# see LICENSE file (it's BSD)
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os


import time
from pygsm import GsmModem

# all arguments to GsmModem.__init__ are optional, and passed straight
# along to pySerial. for many devices, this will be enough:

gmail_user = "internatrails@gmail.com"
gmail_pwd = "mambalam"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   #part = MIMEBase('application', 'octet-stream')
   #part.set_payload(open(attach, 'rb').read())
   #Encoders.encode_base64(part)
   #part.add_header('Content-Disposition',
    #       'attachment; filename="%s"' % os.path.basename(attach))
   #msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

class CountLettersApp(object):
    def __init__(self, modem):
        self.modem = modem

    def incoming(self, msg):
        #msg.respond("Thanks for those %d characters!" %\
            len(msg.text)

    def serve_forever(self):
        while True:
            print "Checking for message..."
            msg = self.modem.next_message()

            if msg is not None:
                print "Got Message: %r" % (msg)
		print msg
                mail("vignesh2510raju@gmail.com",msg.text[:10],msg.text[11:],"")
                self.incoming(msg)

            time.sleep(2)


# all arguments to GsmModem.__init__ are optional, and passed straight
# along to pySerial. for many devices, this will be enough:
gsm = GsmModem(
    port="/dev/ttyUSB0",
    logger=GsmModem.debug_logger).boot()


print "Waiting for network..."
s = gsm.wait_for_network()


# start the demo app
app = CountLettersApp(gsm)
app.serve_forever()
