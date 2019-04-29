"""
SMTP

: SSL - 처음부터 암호화된 통신을 시도
      - 포트번호 465
: TLS - 처음엔 암호화되지 않은 hello 메시지를 전달하는 것에서 시작
      - 포트번호 587

"""
import smtplib
from email.mime.text import MIMEText

TOKEN = 'abcde12345'

sender_id = input('input sender\'s email id except domain.\n')
sender_domain = input('input sender\'s domain except @.\n')
sender_pw = input('input sender\'s password.\n')
sender = sender_id + '@' + sender_domain

receiver = 'chlcgy@naver.com'

smtp = smtplib.SMTP('smtp.' + sender_domain, 587)
smtp.ehlo() # say Hello
smtp.starttls() # start TLS Encryption
smtp.login(sender, sender_pw)

msg = MIMEText(TOKEN)
msg['Subject'] = 'This is an authentication test message'
msg['From'] = sender
msg['To'] = receiver
smtp.sendmail(sender, receiver, msg.as_string())

smtp.quit()
