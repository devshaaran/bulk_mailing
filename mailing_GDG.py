import csv                                     #can use .split also but this is one is much easier in use
import smtplib                                 #import the necessary tools
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_id = 'please enter your mail ID'
email_password = 'please enter your password'

#this is what I sent you a while back,others** leave this not the below but this comment...

subject = 'regarding the python task'  #write your subject here

msg = MIMEMultipart()
msg['From'] = email_id
msg['Subject'] = subject

body = 'Hi there gdgvitvellore , This is shaaran sending this email from Python!!'  #body
msg.attach(MIMEText(body,'plain'))

with open('emails_gdg.csv','r') as csv_gdg:    #opening csv
    csv_gdgreader = csv.reader(csv_gdg)

    for i in csv_gdgreader:
        mail_id = i[1]
        email_send = mail_id
        msg['To'] = email_send
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_id, email_password)
        server.sendmail(email_id, email_send, text)
        server.quit()
