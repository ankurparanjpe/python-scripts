import imaplib, email
import io
import os

#log in and select the inbox
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('ankurparanjpe10@gmail.com', 'qu@ke6arena')
mail.select('testing')

#get uids of all messages
result, data = mail.uid('search', None, 'UNSEEN') 
uids = data[0].split()
print (uids)
#read the lastest message
result, data = mail.uid('fetch', uids[-1], '(RFC822)')
m = email.message_from_string(data[0][1].decode())

if m.get_content_maintype() == 'multipart':
    for part in m.walk():
        if part.get_content_maintype() == 'multipart': continue
        if part.get('Content-Disposition') is None: continue

        filename = part.get_filename()
        if filename is None:
            continue
        fp = open(filename, 'wb')
        fp.write(part.get_payload(decode=True))
        fp.close()
        print (f'{filename} saved!')
