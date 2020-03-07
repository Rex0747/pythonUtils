# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()


message = "Mensaje enviado"

# setup the parameters of the message
password = "Pedro2016"
msg['From'] = "pjimenez@cogesasl.com"
msg['To'] = "peli0747@gmail.com"
msg['Subject'] = "Mensaje a CGS"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP("smtp.office365.com: 587")     #('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)


# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))