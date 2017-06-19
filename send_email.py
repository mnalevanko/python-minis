import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("nalevanko.data@gmail.com", "Lkjtp,tbats.")
 
msg = "Subject: {}\n\n{}".format('Predmet spravy', 'Telo spravy')
server.sendmail("nalevanko.data@gmail.com", "michal.nalevanko@gmail.com", msg)
server.quit()


'''
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "nalevanko.data@gmail.com"
toaddr = "michal.nalevanko@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Today's free e-book: "
 
body = "Sem pride veta s nazvom knihy"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Lkjtp,tbats.")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
'''
