import imaplib
import MySQLdb
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

username='internatrails@gmail.com'
password='mambalam'

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="ssn", db="smsmail")

cursor=db.cursor()
cursor.execute("use smsmail")


#Mail to any person using this function (SMTP)
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

# Get emails for the list of email_ids passed
def get_emails(email_ids):
    data = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(UID BODY[TEXT])')
        data.append(response[0][1])
    return data

# Get only the subjects of the list of email_ids passed
def get_subjects(email_ids):
    subjects = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(body[header.fields (subject)])')
        subjects.append( response[0][1][9:] )

    return subjects

# Get the sender Email ids of the list of email_ids passed
def get_froms(email_ids):
    froms = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(body[header.fields (from)])')
        froms.append( response[0][1][5:] )

    return froms

imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)

imap_server.login(username,password)

# Select the particular mailbox from the list of available mailboxes
imap_server.select('INBOX')

status, response = imap_server.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))
print unreadcount

# Get the list of Unread mails alone
def getunseenmails():
    email_ids = imap_server.search(None,"(UNSEEN)" )
    email_id=(email_ids[1][0].split(' '))
    return email_id

# Get all the mails in the selected mailbox
def getallmails():
    email_ids=imap_server.search(None,"ALL")
    email_id=(email_ids[1][0].split(' '))
    return email_id

# This variable holds the list of all the available mailboxes
folderlist=imap_server.list()


email_id=getallmails()

print email_id



allsubs=get_subjects(email_id)
allfroms=get_froms(email_id)

i=0


# Displaying Sender and the SUbjects of allmails in the mailbox
while i<len(email_id):
    print 'Mail No. :',email_id[i]
    print '\nFrom :'
    print allfroms[i]
    print '\nSubject : '
    print allsubs[i]
    cursor.execute('INSERT INTO mails VALUES (%s,"internatrails@gmail.com",%s,%s,"+919940138729",NULL)',(email_id[i],allfroms[i],allsubs[i]))
    print "Inserted row into database smsmail!" 
    i+=1

'''for i in email_id:
    print allfroms[i]
    print '\n',allsubjects[i]
   ''' 
imap_server.logout()
'''for sub in allsubs:
    print sub
    mail('karthik.s.sundaram@gmail.com',,'Hi this is a program','')'''

