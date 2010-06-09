import imaplib

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


imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)

username='internatrails@gmail.com'
password='mambalam'

imap_server.login('internatrails@gmail.com','mambalam')

imap_server.select('INBOX')

status, response = imap_server.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))
print unreadcount

email_ids = imap_server.search(None,'ALL' )
email_id=(email_ids[1][0].split(' '))

print email_id

allsubs=get_subjects(email_id)

for sub in allsubs:
    print sub
 

