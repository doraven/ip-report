import smtplib
from email.mime.text import MIMEText
from email.headerregistry import Address

import requests, re, time

while(True):
    while(True):
        try:
            s = requests.get('http://1212.ip138.com/ic.asp').text
        except Exception:
            time.sleep(10)
            continue
        else:
            ipre = re.search(r'\[.+\]', s)
            if ipre:
                break
    ip = ipre.group(0)[1:-1]

    last_ip = open('ip.txt', 'r').read()
    if ip and ip != last_ip:
        print(ip)
        send_email(ip)
        open('ip.txt', 'w').write(ip)

    time.sleep(10*60)
#    tm = time.localtime()
#    print('%s:%s:%s'%(tm.tm_hour, tm.tm_min, tm.tm_sec), end = '\t')
#    print(ss.group(0)[1:-1])


def send_email(ip):
    smtpserver = 'smtp.qq.com'
    username = '909353892@qq.com'
    password = 'pwnzcvnrqhirbcib'


    sender = username
    receiver = ['doraven@qq.com',]
    msg = MIMEText(ip)
    msg['Subject'] = 'HOME_IP_CHANGED'
    h = Header('本尊大人')
    h.append('<909353892@qq.com>')

    from_address = Address('本尊大人', '909353892', 'qq.com')
    to_address = ', '.join
    msg['From'] = h
    msg['To'] = receiver


    smtp = smtplib.SMTP_SSL(smtpserver, port = 465)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    return True
