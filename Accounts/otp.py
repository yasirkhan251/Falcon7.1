
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

    msg.set_content("Please enable HTML to view this email.")

    msg.add_alternative(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            margin: 0 !important;
            padding: 0 !important;
            background-color: #000000 !important;
            font-family: 'Outfit', Arial, Helvetica, sans-serif;
            color: #ffffff;
            -webkit-font-smoothing: antialiased;
        }}

        /* Full width wrapper to force background color in Gmail */
        .wrapper {{
            width: 100%;
            table-layout: fixed;
            background-color: #000000;
            padding-bottom: 40px;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: #0a0a0a;
            border: 1px solid #222222;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
        }}

        .header {{
            background: #111111;
            padding: 25px;
            text-align: center;
            border-bottom: 2px solid #3b82f6;
        }}

        .header h1 {{
            margin: 0;
            font-size: 26px;
            color: #ffffff;
        }}

        .content {{
            padding: 35px;
            color: #e2e8f0;
        }}

        .content h2 {{
            margin-top: 0;
            color: #ffffff;
        }}

        .otp {{
            background: #111111;
            border: 2px dashed #3b82f6;
            text-align: center;
            font-size: 36px;
            letter-spacing: 12px;
            font-weight: bold;
            color: #f97316;
            padding: 20px;
            margin: 30px 0;
            border-radius: 12px;
        }}

        .info {{
            background: #111111;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            border-left: 4px solid #3b82f6;
        }}

        .info table {{
            width: 100%;
            color: #e2e8f0;
        }}

        .info td {{
            padding: 8px 0;
        }}
        
        .info td strong {{
            color: #94a3b8;
        }}

        .warning {{
            margin-top: 30px;
            background: rgba(249, 115, 22, 0.1);
            color: #fbd38d;
            border-left: 4px solid #f97316;
            padding: 18px;
            border-radius: 6px;
            font-size: 14px;
            line-height: 1.6;
        }}

        .footer {{
            text-align: center;
            font-size: 13px;
            color: #64748b;
            padding: 20px;
            background: #111111;
            border-top: 1px solid #222222;
        }}
    </style>
</head>

<body style="background-color: #000000; margin: 0; padding: 0;">

<!-- This wrapper table acts as the true "body" for email clients -->
<table class="wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation" style="background-color: #000000;">
    <tr>
        <td align="center" style="padding-top: 40px; padding-bottom: 40px;">
            
            <table class="container" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="max-width: 600px; text-align: left;">
                <tr>
                    <td>
                        <div class="header">
                            <h1>Authentication System</h1>
                        </div>

                        <div class="content">
                            <h2>Hello, {name} 👋</h2>

                            <p>
                                We received a request to verify your account.
                                Please use the One-Time Password (OTP) below to continue.
                            </p>

                            <div class="otp">
                                {otp}
                            </div>

                            <div class="info">
                                <table cellpadding="0" cellspacing="0" role="presentation">
                                    <tr>
                                        <td width="60"><strong>Email:</strong></td>
                                        <td>{email}</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Phone:</strong></td>
                                        <td>{phone}</td>
                                    </tr>
                                </table>
                            </div>

                            <div class="warning">
                                <strong style="color: #f97316; font-size: 16px;">Security Notice</strong><br><br>

                                • Never share your OTP with anyone.<br>
                                • Our team will never ask for your OTP.<br>
                                • If you didn't request this verification, you can safely ignore this email.
                            </div>
                        </div>

                        <div class="footer">
                            © 2026 Authentication System<br>
                            This is an automated email. Please do not reply.
                        </div>
                    </td>
                </tr>
            </table>

        </td>
    </tr>
</table>

</body>
</html>
""", subtype="html")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender_email, app_password)

        smtp.send_message(msg)

    print("\n✅ Email Sent Successfully!\n")
    
    
    
    


# file end 