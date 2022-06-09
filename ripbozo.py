from wikipedia import summary, search, exceptions
from colorama import init, Fore, Style
from dotenv import load_dotenv
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys
import time
import smtplib

#colorama init
init()

#env variables
load_dotenv()
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#function to send email
def sendMail(name, recipient):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #smtp init
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        #compose message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'{name} has died.'
        msg['From'] = 'RIP BOZO'
        msg['To'] = recipient
        html = f'<html><body><h1>RIP. {name}</h1></body></html>'
        msg.attach(MIMEText(html, 'html'))

        smtp.send_message(msg)
        print('Email sent.')
        smtp.quit()
    

#open file with names and recipients
try:
    namesFile = open(sys.argv[1])
    recipientsFile = open(sys.argv[2])
except:
    print('Please supply a file with names and recipients.')
    exit()

names = namesFile.read().split('\n')
recipients = recipientsFile.read().split('\n')


#main loop
for name in names:
    if name: 
        dead = False
        try:
            summaryArr = summary(name, sentences=2, auto_suggest=False).split()
        except exceptions.PageError:
            print(name + ' not found.')
            continue

        for word in summaryArr:
            if word == 'was':
                dead = True
                break
            if word == 'is':
                break
        
        msg = 'Alive'
        color = Fore.GREEN
        if dead:
            msg = 'Deceased'
            color = Fore.RED

            for recipient in recipients:
                if recipient:
                    sendMail(name, recipient)
            
            #remove name to avoid repeated notifications
            file = open(sys.argv[1], 'rt')
            data = file.read()
            data = data.replace(name, '')
            file.close()
            file = open(sys.argv[1], 'wt')
            file.write(data)
            file.close()


        print(name + ': ' + color + msg + Style.RESET_ALL)
