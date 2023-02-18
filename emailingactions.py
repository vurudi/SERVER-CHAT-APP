
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import socket


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER = ''
with open('SERVERMAIL.txt', 'r') as f:
    SENDER = f.read()
    reciepient='paxpaxpax100@gmail.com'


class AutomatedEmails:
    def approval_mail(sender, recipient):
        """ Send email message """
        msg = MIMEMultipart()
        msg['Subject'] = 'VURUDI100 SOFTWARE SPOT approval!'
        msg['To'] = recipient
        msg['From'] = sender

        # attach image files
        otp = 887654
        with open('messege.txt', 'r') as f:
            messege = f.read()
            messege = messege + f' your password is :{otp}   Email: paxpaxpax100@gmail.com'
        msg.attach(MIMEText(messege, 'plain'))
        filename = 'vurudi100.jpg'
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(p)
        text = msg.as_string()
        # smtp connectioncall
        AutomatedEmails.session0(sender, recipient, text)

    def otp_mail(sender, recipient):
        """ Send otp message """

        msg = MIMEMultipart()
        msg['Subject'] = 'CHAT APP ACCOUNT CREATION APPROVAL!'
        msg['To'] = recipient
        msg['From'] = sender

        # attach image files
        otp = 887654
        with open('OTPmessege.txt', 'r') as f:
            messege = f.read()
            messege = messege + f' Auto generated OTP is:  {otp} '
            # smtp connectioncall
            AutomatedEmails.session0(sender, recipient, messege)

    def restore_pass(sender, reciepient):
        """ Send email message """
        msg = MIMEMultipart()
        msg['Subject'] = 'CHAT EXPERT PASSWORD retrieval!'
        msg['To'] = reciepient
        msg['From'] = sender

        # attach image files
        retrieved = 887654
        with open('retrieve_message.txt', 'r') as f:
            retrive_message = f.read()
            retrive = retrive_message + f' Your password is :{retrieved} \n\nAlways keep your' \
                                        f'password secrete \n '
        msg.attach(MIMEText(retrive, 'plain'))
        filename = 'chatexpert.png'
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(p)
        text = msg.as_string()
        # smtp connectioncall
        AutomatedEmails.session0(sender, reciepient, text)

        # create smtp session

    def session0(sender, reciepient, text):
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        with open('gmaillogpass.txt', 'r') as f:
            password = f.read()
        session.login(sender, password)
        session.sendmail(sender, reciepient, text)
        print("password sent !!.")
        session.quit()
