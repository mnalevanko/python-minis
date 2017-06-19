import smtplib

host = 'smtp.gmail.com'
port = 587
username = 'nalevanko.data@gmail.com'
password = 'Lkjtp,tbats(Mt6:21)'
from_email = username
to_list = ['michal.nalevanko@gmail.com']

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, 'Hello there!\nThis is an email message')
email_conn.quit()

from smtplib import SMTP

