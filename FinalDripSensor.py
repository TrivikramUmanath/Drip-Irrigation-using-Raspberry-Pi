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
def Tulsi(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        if board.analog[0].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[0].read())<=.3418):
                board.digital[led_pin1].write(1)
                print('Watering Tulsi')
                print(board.analog[0].read())
            board.digital[led_pin1].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        if board.analog[0].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[0].read())<=0.1953):
                board.digital[led_pin1].write(1)
                print('Watering Tulsi')
                print(board.analog[0].read())
            board.digital[led_pin1].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        if board.analog[0].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[0].read())<=0.4404):
                board.digital[led_pin1].write(1)
                print('Watering Tulsi')
                print(board.analog[0].read())
            board.digital[led_pin1].write(0)      
def Shoeplant(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[1].enable_reporting()
        if board.analog[1].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[1].read())<=0.3030):
                board.digital[led_pin2].write(1)
                print('Watering Shoeplant')
                print(board.analog[1].read())
            board.digital[led_pin2].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[1].enable_reporting()
        if board.analog[1].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[1].read())<=0.1464):
                board.digital[led_pin2].write(1)
                print('Watering Shoeplant')
                print(board.analog[1].read())
            board.digital[led_pin2].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[1].enable_reporting()
        if board.analog[1].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[1].read())<=0.3906):
                board.digital[led_pin2].write(1)
                print('Watering Shoeplant')
                print(board.analog[1].read())
            board.digital[led_pin2].write(0)  
def Moneyplant(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[2].enable_reporting()
        if board.analog[2].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[2].read())<=0.3417):
                board.digital[led_pin3].write(1)
                print('Watering Moneyplant')
                print(board.analog[2].read())
            board.digital[led_pin1].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[2].enable_reporting()
        if board.analog[2].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[2].read())<=.19531):
                board.digital[led_pin3].write(1)
                print('Watering Moneyplant')
                print(board.analog[2].read())
            board.digital[led_pin1].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[2].enable_reporting()
        if board.analog[2].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[2].read())<=0.43945):
                board.digital[led_pin3].write(1)
                print('Watering Moneyplant')
                print(board.analog[2].read())
            board.digital[led_pin1].write(0)      
def Jade(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[3].enable_reporting()
        if board.analog[3].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[3].read())<=.3417):
                board.digital[led_pin1].write(1)
                print('Watering Jade')
                print(board.analog[3].read())
            board.digital[led_pin1].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[3].enable_reporting()
        if board.analog[3].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[3].read())<=.19531):
                board.digital[led_pin4].write(1)
                print('Watering Jade')
                print(board.analog[3].read())
            board.digital[led_pin4].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[3].enable_reporting()
        if board.analog[3].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[3].read())<=.43945):
                board.digital[led_pin4].write(1)
                print('Watering Jade')
                print(board.analog[3].read())  
            board.digital[led_pin4].write(0)
def midTulsi(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        if board.analog[0].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[0].read())<=.6836):
                board.digital[led_pin1].write(1)
                print('Watering Tulsi')
                print(board.analog[0].read())
            board.digital[led_pin1].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        if board.analog[0].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[0].read())<=0.3906):
                board.digital[led_pin1].write(1)
                print('Watering Tulsi')
                print(board.analog[0].read())  
            board.digital[led_pin1].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        if board.analog[0].read() is None:
            print('Something wrong')
        else:
            while(float(board.analog[0].read())<=0.8808):
                board.digital[led_pin1].write(1)
                print('Watering Tulsi')
                print(board.analog[0].read())  
            board.digital[led_pin1].write(0)
def midShoePlant(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[1].enable_reporting()
        if board.analog[1].read() is None:
            print('Something wrong')
        else: 
            while(float(board.analog[1].read())<=0.6060):
                board.digital[led_pin2].write(1)
                print('Watering Shoeplant')
                print(board.analog[1].read())   
            board.digital[led_pin2].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[1].enable_reporting()
        if board.analog[1].read() is None:
            print('Something wrong')
        else:   
            while(float(board.analog[1].read())<=0.2928):
                board.digital[led_pin2].write(1)
                print('Watering Shoeplant')
                print(board.analog[1].read())   
            board.digital[led_pin2].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[1].enable_reporting()
        if board.analog[1].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[1].read())<=0.7812):
                board.digital[led_pin2].write(1)
                print('Watering Shoeplant')
                print(board.analog[1].read())
            board.digital[led_pin2].write(0)
def midMoneyPlant(month):
     if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[2].enable_reporting()
        if board.analog[2].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[2].read())<=0.6834):
                board.digital[led_pin3].write(1)
                print('Watering Moneyplant')
                print(board.analog[2].read())  
            board.digital[led_pin1].write(0)
     elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[2].enable_reporting()
        if board.analog[2].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[2].read())<=.39062):
                board.digital[led_pin3].write(1)
                print('Watering Moneyplant')
                print(board.analog[2].read())  
            board.digital[led_pin1].write(0)
     elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[2].enable_reporting()
        if board.analog[2].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[2].read())<=0.8789):
                board.digital[led_pin3].write(1)
                print('Watering Moneyplant')
                print(board.analog[2].read())    
            board.digital[led_pin3].write(0)
def midJade(month):
    if month==1 or month>=10:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[3].enable_reporting()
        if board.analog[3].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[3].read())<=.6834):
                board.digital[led_pin1].write(1)
                print('Watering Jade')
                print(board.analog[3].read())   
            board.digital[led_pin1].write(0)
    elif month>=2 and month<=5:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[3].enable_reporting()
        if board.analog[3].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[3].read())<=.39062):
                board.digital[led_pin4].write(1)
                print('Watering Jade')
                print(board.analog[3].read())    
            board.digital[led_pin4].write(0)
    elif month>=6 and month<=9:
        it = pyfirmata.util.Iterator(board)
        it.start()
        board.analog[3].enable_reporting()
        if board.analog[3].read() is None:
            print('Something wrong')
        else:    
            while(float(board.analog[3].read())<=.8789):
                board.digital[led_pin4].write(1)
                print('Watering Jade')
                print(board.analog[3].read())  
            board.digital[led_pin4].write(0)
    
print ('Code is running')            
while True:
    month=time.strftime("%m",time.localtime())#Taking the month
    month=int(month)
    if month==1 or month>=10:#comparing the month(if Winter)
        print('Winter')
        hr=time.strftime("%H",time.localtime())#taking the hour
        print(hr)
        hr=int(hr)#converting string to int
        minu=time.strftime("%M",time.localtime())#taking the minute
        minu=int(minu)
        sec=time.strftime("%S",time.localtime())
        sec=int(sec)
        if hr==7 and minu==59 and sec==0:
            s.sendmail(fromAdd, toAdd,"You can water all the plants in one minute.")
            print('Mail sent')
        elif hr==8 and minu==0:#comparing hours and minutes
            if(a!=1):
                Tulsi(month)
            elif(b!=2):   
                Shoeplant(month)
            elif(c!=3):    
               MoneyPlant(month)
            elif(d!=4):   
                Jade(month)
            a=0
            b=0
            c=0
            d=0
            time.sleep(60)
        elif hr==14 and minu==0:
            midTulsi(month)
            midShoePlant(month)
            midMoneyPlant(month)
            midJade(month)
            time.sleep(60)
        elif hr==16 and minu==29 and sec==0:
            s.sendmail(fromAdd, toAdd,"You can water Tulsi and Shoeplant in one minute.")
            print('Mail sent')
            time.sleep(2)
        elif hr==16 and minu==30:
            if(a!=1):
                Tulsi(month)
            elif(b!=2):   
                Shoeplant(month)
            a=0
            b=0
            c=0
            d=0
            time.sleep(60)
        elif (hr==7 and minu<=59 and sec<=50) or(hr==16 and minu<=29 and sec<=50):
            if GPIO.input(18)==1:
                Tulsi(month)
                a=1
            elif GPIO.input(23)==1:
               Shoeplant(month)
               b=2
            elif (GPIO.input(24)==1) and (hr==7 and minu<=59 and sec<=50):
                Moneyplant(month)
                c=3
            elif GPIO.input(25)==1 and (hr==7 and minu<=59 and sec<=50):
                Jade(month)
                d=4
            sec=time.strftime("%S",time.localtime())
            sec=int(sec)   
    elif month>=2 and month<=5:#comparing months(Summer)
        hr=time.strftime("%H",time.localtime())#taking the hour
        print('Summer')
        hr=int(hr)
        minu=time.strftime("%M",time.localtime())#taking the minute
        minu=int(minu)
        sec=time.strftime("%S",time.localtime())
        sec=int(sec) 
        if hr==7 and minu==59 and sec==0:
            s.sendmail(fromAdd, toAdd,"You can water all the plants in one minute.")
            print("Mail")
        elif hr==8 and minu==0:
            if(a!=1):
                Tulsi(month)
            elif(b!=2):   
                Shoeplant(month)
            elif(c!=3):    
                MoneyPlant(month)
            elif(d!=4):   
                Jade(month)
            a=0
            b=0
            c=0
            d=0
            time.sleep(60)
        elif hr==14 and minu==0:
            midTulsi()
            midShoePlant(month)
            midMoneyPlant(month)
            midJade(month)
            time.sleep(60)
        elif hr==16 and minu==29 and sec==0:
            s.sendmail(fromAdd, toAdd,"You can water Tulsi,Shoeplant and Jade in one minute.")
            s.quit()
            print('MAIL SENT')
            time.sleep(2)
        elif hr==16 and minu==30:
            if(a!=1):
                Tulsi(month)
            elif(b!=2):   
                Shoeplant(month)
            elif(c!=3):    
                MoneyPlant(month)
            a=0
            b=0
            c=0
            d=0
            time.sleep(60)
        elif (hr==7 and minu<=59 and sec<=50) or(hr==23 and minu<=59 and sec<=50):
            if GPIO.input(18)==1:
                Tulsi(month)
                a=1
            elif GPIO.input(23)==1:
                Shoeplant(month)
                b=2
            elif GPIO.input(24)==1:
                Moneyplant(month)
                c=3
            elif (GPIO.input(25)==1) and (hr==7 and minu<=59 and sec<=50):
                Jade(month)
                d=4
            sec=time.strftime("%S",time.localtime())
            sec=int(sec)    
    elif month>=6 and month<=9:#comparing months(Monsoon)
        hr=time.strftime("%H",time.localtime())#taking the hour
        print('Monsoon')
        hr=int(hr)
        minu=time.strftime("%M",time.localtime())#taking the minute
        minu=int(minu)
        if hr==7 and minu==59 and sec==0:
            s.sendmail(fromAdd, toAdd,"You can water all the plants in one minute.")
        elif hr==8 and minu==0:#comparing hours and minutes
            if(a!=1):
                Tulsi(month)
            elif(b!=2):   
                Shoeplant(month)
            elif(c!=3):    
                MoneyPlant(month)
            elif(d!=4):   
                Jade(month)
            a=0
            b=0
            c=0
            d=0
            time.sleep(60)
        elif hr==14 and minu==0:
            midTulsi(month)
            midShoePlant(month)
            midMoneyPlant(month)
            midJade(month)
            time.sleep(60)
        elif (hr==7 and minu<=59  and sec<=50):
            if GPIO.input(18)==1:
                Tulsi(month)
                a=1
            elif GPIO.input(23)==1:
               Shoeplant(month)
               b=2
            elif GPIO.input(24)==1:
                Moneyplant(month)
                c=3
            elif GPIO.input(25)==1:
               Jade(month)
               d=4
            sec=time.strftime("%S",time.localtime())
            sec=int(sec)         
            
           
            
