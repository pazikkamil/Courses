# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

from __future__ import unicode_literals

from imapclient import IMAPClient
import os

HOST = 'imap.gmail.com'
#HOST = 'imap.wp.pl'
USERNAME = os.environ.get('GMAIL_USER')
PASSWORD = os.environ.get('GMAIL_PASSWD')
ssl = True


# def get_past_emails(self, folder, from_date=None, to_date=None, from_person=None, to_person=None):
#    """Get past emails from/to given date/person"""

# IF wp.pl -> use_uid = False
# IF gmail -> use_uid = True
server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

folders_list = server.list_folders()

#server.search(u'(HEADER TO "{}")'.format("alicja.karalus@instream.io")))

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info['EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))

print()
print("Messages:")
response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
for msgid, data in response.iteritems():
    print('   ID %d: %d bytes, flags=%s' % (msgid,
                                            data[b'RFC822.SIZE'],
                                            data[b'FLAGS']))