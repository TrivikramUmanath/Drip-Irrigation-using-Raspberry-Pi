import pyfirmata
import time
import RPi.GPIO as GPIO
import BlynkLib
import smtplib
import imghdr
from email.message import EmailMessage
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)
board = pyfirmata.Arduino('/dev/ttyACM0')
led_pin1=13#pin for tulsi
led_pin2=12#pin for shoeplant
led_pin3=11#pin for moneyplant
led_pin4=10#pin for Jade
smtpUser = "irigationdrip48@gmail.com"
smtpPass = "password125"
toAdd = "vikram.umanath@gmail.com"
fromAdd= smtpUser
msg = EmailMessage()
msg['From'] = smtpUser
msg['To'] = toAdd
msg['Subject'] ='Watering the plants'
s= smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(smtpUser,smtpPass) 
def Tulsi():
    board.digital[led_pin1].write(1)#watering tulsi
    print('Watering Tulsi')
    board.pass_time(3)
    board.digital[led_pin1].write(0)
def Shoeplant():
    board.digital[led_pin2].write(1)#watering shoeplant
    print('Watering Shoeplant')
    board.pass_time(4)
    board.digital[led_pin2].write(0)
def Moneyplant():
    board.digital[led_pin3].write(1)#watering moneyplant
    print('Watering moneyplant')
    board.pass_time(4)        
    board.digital[led_pin3].write(0)
def Jade():
    board.digital[led_pin4].write(1)#watering Jade
    print('Watering Jade')
    board.pass_time(3)        
    board.digital[led_pin4].write(0)
   
    
print ('Code is running')            
while True:
    a=time.strftime("%m",time.localtime())#Taking the month
    a=int(a)
    if a==1 or a>=10:#comparing the month(if Winter)
        print('Winter')
        b=time.strftime("%H",time.localtime())#taking the hour
        print(b)
        b=int(b)#converting string to int
        c=time.strftime("%M",time.localtime())#taking the minute
        c=int(c)
        d=time.strftime("%S",time.localtime())
        d=int(d)
        if b==7 and c==59 and d==0:
            s.sendmail(fromAdd, toAdd,"You can water all the plants in one minute.")
            print('Mail sent')
        elif b==8 and c==0:#comparing hours and minutes
            Tulsi()
            Shoeplant()
            MoneyPlant()
            Jade()
            time.sleep(60)
        elif b==16 and c==29 and d==0:
            s.sendmail(fromAdd, toAdd,"You can water Tulsi and Shoeplant in one minute.")
            print('Mail sent')
            time.sleep(2)
        elif b==16 and c==30:
            Tulsi()
            Shoeplant()
            MoneyPlant()
            Jade()
            time.sleep(60)
        elif (b==7 and c<=59 and d<=50) or(b==16 and c<=29 and d<=50):
            if GPIO.input(18)==1:
                Tulsi()
            elif GPIO.input(23)==1:
               Shoeplant()
            elif (GPIO.input(24)==1) and (b==7 and c<=59 and d<=50):
                Moneyplant()
            elif GPIO.input(25)==1 and (b==7 and c<=59 and d<=50):
                Jade()
            d=time.strftime("%S",time.localtime())
            d=int(d)   
    elif a>=2 and a<=5:#comparing months(Summer)
        b=time.strftime("%H",time.localtime())#taking the hour
        print('Summer')
        b=int(b)
        c=time.strftime("%M",time.localtime())#taking the minute
        c=int(c)
        d=time.strftime("%S",time.localtime())
        d=int(d) 
        if b==7 and c==59 and d==0:
            s.sendmail(fromAdd, toAdd,"You can water all the plants in one minute.")
            print("Mail")
        elif b==15 and c==49:#comparing hours and minutes
            Tulsi()
            Shoeplant()
            Moneyplant()
            Jade()
            time.sleep(60)
        elif b==16 and c==59 and d==0:
            s.sendmail(fromAdd, toAdd,"You can water Tulsi,Shoeplant and Jade in one minute.")
            s.quit()
            print('MAIL SENT')
            time.sleep(2)
        elif b==16 and c==30:
            Tulsi()
            Shoeplant()
            MoneyPlant()
            time.sleep(60)
        elif (b==7 and c<=59 and d<=50) or(b==16 and c<=59 and d<=50):
            if GPIO.input(18)==1:
              Tulsi()
            elif GPIO.input(23)==1:
                Shoeplant()
            elif GPIO.input(24)==1:
                Moneyplant()
            elif (GPIO.input(25)==1) and (b==7 and c<=59 and d<=50):
                Jade()
            d=time.strftime("%S",time.localtime())
            d=int(d)    
    elif a>=6 and a<=9:#comparing months(Monsoon)
        b=time.strftime("%H",time.localtime())#taking the hour
        print('Monsoon')
        b=int(b)
        c=time.strftime("%M",time.localtime())#taking the minute
        c=int(c)
        if b==7 and c==59 and d==0:
            s.sendmail(fromAdd, toAdd,"You can water all the plants in one minute.")
        elif b==8 and c==0:#comparing hours and minutes
            Tulsi()
            Shoeplant()
            MoneyPlant()
            Jade()
            time.sleep(60)
        elif (b==7 and c<=59  and d<=50):
            if GPIO.input(18)==1:
                Tulsi()
            elif GPIO.input(23)==1:
               Shoeplant()
            elif GPIO.input(24)==1:
                Moneyplant()
            elif GPIO.input(25)==1:
               Jade() 
            d=time.strftime("%S",time.localtime())
            d=int(d)         
            
           
            
