import re


def fetch_emails_from_doc(file_name):
    distinct_mails = []
    try:
        file_content = open(file_name).read()
        mails = re.findall('[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+', file_content)
        [distinct_mails.append(m) for m in mails if m not in distinct_mails]
    except FileNotFoundError:
        print('File Not Found')
    except:
        print('Error Occurred!!!')
    return distinct_mails


emails = fetch_emails_from_doc('Lab6_Webpage.html')
print(f'Distinct emails in the document : {emails}')
