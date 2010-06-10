import imaplib

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

username='internatrails@gmail.com'
password='mambalam'

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = username
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))
   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(username,password)
   mailServer.sendmail(username, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()


def get_emails(email_ids):
    data = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(UID BODY[TEXT])')
        data.append(response[0][1])
    return data

def get_subjects(email_ids):
    subjects = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(body[header.fields (subject)])')
        subjects.append( response[0][1][9:] )

    return subjects

def get_froms(email_ids):
    froms = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(body[header.fields (from)])')
        froms.append( response[0][1][5:] )

    return froms

imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)

imap_server.login(username,password)

imap_server.select('INBOX')

status, response = imap_server.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))
print unreadcount

email_ids = imap_server.search(None,'ALL' )
email_id=(email_ids[1][0].split(' '))

print email_id

allsubs=get_froms(email_id)

for sub in allsubs:
    print sub
 
imap_server.logout()
'''for sub in allsubs:
    print sub
    mail('karthik.s.sundaram@gmail.com',,'Hi this is a program','')'''

