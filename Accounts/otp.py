
import random,json
from django.contrib import messages
from email.message import EmailMessage
import smtplib
CREDENTIALS = "cred.json"

with open(CREDENTIALS, "r") as cred:
    credentials = json.load(cred)


def generate_otp():
    return random.randint(100000,999999)
     

def send_otp(name,email,phone,otp):

    send_email(email,otp,name,phone)
    
    
    
    

def send_email(email, otp, name, phone):

    sender_email = credentials[0]["sender_email"]
    app_password = credentials[0]["Appcode"]

    msg = EmailMessage()

    msg["Subject"] = "OTP Verification"
    msg["From"] = sender_email
    msg["To"] = email

    msg.set_content(f"""
Hi {name},

Your One-Time Password (OTP) is:

{otp}

You can login using:

Email : {email}
Phone : {phone}

This OTP is confidential.

Please do not share it with anyone.

Regards,
Authentication System
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender_email, app_password)

        smtp.send_message(msg)

    print("\n✅ Email Sent Successfully!\n")