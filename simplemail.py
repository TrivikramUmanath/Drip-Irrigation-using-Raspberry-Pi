import smtplib
import imghdr
import time
from email.message import EmailMessage

smtpUser = "irigationdrip48@gmail.com"
smtpPass = "password125"


toAdd = "mahesh.warang@somaiya.edu"
fromAdd= smtpUser

msg = EmailMessage()
msg['From'] = smtpUser
msg['To'] = toAdd
msg['Subject'] ='hELP ME'
s= smtplib.SMTP('smtp.gmail.com',587)
print("HelloSir")
#s.ehlo()
s.starttls()
#s.ehlo()
s.login(smtpUser,smtpPass)
print("HELP")
s.sendmail(fromAdd, toAdd,"Jel")
time.sleep(4)
s.sendmail(fromAdd, toAdd,"WEEEEel")
s.quit()
