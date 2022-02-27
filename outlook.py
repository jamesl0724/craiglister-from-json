from imapclient import IMAPClient
import email

host = 'outlook.office365.com'
user = 'clpostingtest@outlook.com'
password = 'Tyler.1969'
ssl = True

server = IMAPClient(host, use_uid=True, ssl=ssl)
server.login(user, password)

inboxInfo = server.select_folder('INBOX')
messages = server.search(['FROM', 'robot@craigslist.org'])
response = server.fetch(messages, ['RFC822', 'BODY[TEXT]']).items()
link_path = ''
for msgid, data in response:
    for key in data:
        if(key.decode('utf-8') == 'BODY[TEXT]'):
            print(link_path)
            link_path = data[key].decode('utf-8').split('https')[1]
    # print(data.split("https")[1])
    # parsedEmail = email.message_from_string(data['RFC822'])
    # body = email.message_from_string(data['BODY[TEXT]'.encode("utf-8")])
    # parsedBody = parsedEmail.get_payload(0)
    # print (parsedBody)
print(link_path)
server.logout()