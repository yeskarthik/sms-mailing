import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="ssn", db="smsmail")

cursor=db.cursor()


import time
from pygsm import GsmModem

gsm = GsmModem(
    port="/dev/ttyUSB0",
    logger=GsmModem.debug_logger).boot()


cursor.execute('select * from mails where sent=0')
data=cursor.fetchall()

msg=[]


i=0

for row in data:
    mess=str(row[2]+'\n'+row[3])
    ids=row[0]
    msg.append((ids,mess))
    
    i+=1

for ids,mess in msg:
    print ids,mess
    gsm.send_sms('+919940138729',mess)
    cursor.execute('update mails set sent=1 where mailid=%s',ids)

#print mailid,email,fromid,subject,mobile,idm

