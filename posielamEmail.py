from time import sleep
import smtplib

mailing_list = ['tothova.silvia@gmail.com', 'michal.nalevanko@gmail.com']

#print(adresa)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('nalevanko.data@gmail.com', 'Lkjtp,tbats.')
predmet = 'Ahoj zlatko'
telo = 'Toto je telo emailu.'
msg = 'Subject: {}\n\n{}'.format(predmet, telo)
server.sendmail('nalevanko.data@gmail.com', mailing_list, msg)
server.quit()
