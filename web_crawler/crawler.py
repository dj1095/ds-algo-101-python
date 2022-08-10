import re
from urllib.request import urlopen


def fetch_distinct_emails(content):
    distinct_mails = []
    mails = re.findall('[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+', content)
    [distinct_mails.append(m) for m in mails if m not in distinct_mails]
    return distinct_mails


def fetch_emails_from_doc(file_path):
    file_content = ''
    try:
        file_content = open(file_path).read()
    except FileNotFoundError:
        print('File Not Found')
    except:
        print('Error Occurred!!!')
    return fetch_distinct_emails(file_content)


def fetch_emails_from_url(url):
    content = urlopen(url).read().decode()
    return fetch_distinct_emails(content)


emails_doc = fetch_emails_from_doc('Lab6_Webpage.html')
print(f'Distinct emails in the document : {emails_doc}')
print(f' Total number of distinct emails in the document : {len(emails_doc)}')

emails_url = fetch_emails_from_url(' http://e-mailid.blogspot.com/')
print(f'Distinct emails in the url : {emails_url}')
print(f'Total number of distinct emails in the document : {len(emails_url)}')
