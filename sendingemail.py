import smtplib

gmail_user = 'michal.nalevanko@gmail.com'  
gmail_password = 'VsMNabvMZm34'

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:  
    print('Something went wrong...')
