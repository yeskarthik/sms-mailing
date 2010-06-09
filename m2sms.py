import imaplib,getpass


import time
from pygsm import GsmModem


def get_emails(email_ids):
    data = []
    for e_id in email_ids:
        _, response = M.fetch(e_id, '(UID BODY[TEXT])')
        data.append(response[0][1])
    return data

def get_subjects(email_ids):
    subjects = []
    for e_id in email_ids:
        _, response = M.fetch(e_id, '(body[header.fields (subject)])')
        subjects.append( response[0][1][9:] )
    return subjects


'''gsm = GsmModem(
    port="/dev/ttyUSB0",
    logger=GsmModem.debug_logger).boot()
'''

M=imaplib.IMAP4_SSL('imap.gmail.com',993)
#username = str(raw_input('\nUsername :'))
#password = str(getpass.getpass())

M.login('internatrails@gmail.com','mambalam')
#M.login(getpass.getuser(),getpass.getpass())
#M.login(username,password)

M.select()



status, response = M.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))
print unreadcount


status, email_ids = M.search(None,'UNSEEN')
print email_ids
subjects = []
for e_id in email_ids:
    _, response = M.fetch(e_id, '(body[header.fields (subject)])')
    subjects.append( response[0][1][9:] )
print subjects
    



'''
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    sp=data[0][1].find('Subject:')
    fp=data[0][1].find('From:')
    tp=data[0][1].find('To:')
    if sp+140>fp:
      ap=fpt
    else:
      ap=sp+140
    subject=data[0][1][sp:ap]
    fromp=data[0][1][fp:tp]
    print fromp+'\n'+subject, ' Sending SMS to subscribed number'
    gsm.send_sms('+919940138729',fromp+'\n'+subject)	
    #print 'Message %s\n%s\n' % (num, data[0][1])
'''

M.close()
M.logout()


