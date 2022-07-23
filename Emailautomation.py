import smtplib
import smtplib as s
import os
import imghdr
import datetime
from email.message import EmailMessage

def sendingEmail(Receiver, fileName):
    Email_Address = "sujeeshsreebalan45@gmail.com"
    Email_password = "Es53c1Nb5"

    date = str(datetime.date.today())
    msg = EmailMessage()
    msg['Subject'] = "Attendance Sheet of "+date
    msg['From'] = Email_Address
    msg['To'] = Receiver
    msg.set_content("Today's attendance")

    files = ['C:\\Users\\DELL\\FaceRecoginition\\venv\\{}'.format(fileName)]

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype='Attendance', subtype= "octet-stream", filename=fileName)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(Email_Address, Email_password)

        smtp.send_message(msg)

        print("sent successfully...")
