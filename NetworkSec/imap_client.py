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


def get_past_emails(folder="", from_date="", to_date="", from_person="", to_person=""):
    """Get past emails from/to given date/person"""
    global HOST
    global USERNAME
    global PASSWORD
    server = IMAPClient(HOST, use_uid=True, ssl=ssl)
    server.login(USERNAME, PASSWORD)
    # IF wp.pl -> use_uid = False
    # IF gmail -> use_uid = True
    imap_query_start = u"("
    imap_query_end = ")"
    imap_query=""


    #folders_list = server.list_folders()
    if folder is None:
        folder = b'INBOX'

    select_info = server.select_folder(folder)

    if from_person:
        imap_query += 'FROM {}'.format(from_person)
    if to_person:
        imap_query += ' TO {}'.format(to_person)
    if from_date:
        imap_query += ' SINCE {}'.format(from_date)
    if to_date:
        imap_query += ' BEFORE {}'.format(to_date)

    if len(imap_query) > 0:
        imap_query = "{}{}{}".format(imap_query_start, imap_query, imap_query_end)
        messages = server.search(imap_query)
    else:
        messages = server.search()

    # search_query = "{} {} {} {} {} {}".format(
    #     imap_query_start,
    #     imap_from,
    #     imap_to,
    #     imap_since,
    #     imap_before,
    #     imap_query_end
    # )


    #print('%d messages in INBOX' % select_info['EXISTS']) # or b'EXISTS'

    # messages = server.search(['NOT', 'DELETED'])
    # print("%d messages that aren't deleted" % len(messages))

    print()
    print("Messages:")
    response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
    for msgid, data in response.items():
    #for msgid, data in response.iteritems():
        print('   ID %d: %d bytes, flags=%s' % (msgid,
                                                data[b'RFC822.SIZE'],
                                                data[b'FLAGS']))

x = get_past_emails(b'INBOX',from_person='kamil.pazik@instream.io', from_date='01-JAN-2017')