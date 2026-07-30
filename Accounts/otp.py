
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
    
    
    
    
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Import your User model if it's custom, or standard Django auth model

# def verify_otp(request):
#     if request.method == "POST":
#         submitted_otp = request.POST.get("otp")
#         new_password = request.POST.get("new_password")
#         confirm_password = request.POST.get("confirm_password")

#         # Get session data
#         session_otp = request.session.get("otp")
#         user_id = request.session.get("otp_user_id")
#         email = request.session.get("otp_email")
        
#         # 1. Check if session expired
#         if not session_otp or not user_id:
#             messages.error(request, "Session expired. Please request a new OTP.")
#             return redirect('forgot_password') # Change to your forgot password URL name

#         # 2. Validate OTP
#         if submitted_otp != session_otp:
#             messages.error(request, "Invalid OTP. Please try again.")
#             return render(request, 'Auth/otpverification.html', {'email': email})

#         # 3. Validate Passwords
#         if new_password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#             return render(request, 'Auth/otpverification.html', {'email': email})
            
#         if len(new_password) < 6:
#             messages.error(request, "Password must be at least 6 characters.")
#             return render(request, 'Auth/otpverification.html', {'email': email})

#         # 4. Update the Password
#         try:
#             # Assuming you have a way to fetch the user by ID
#             # Replace 'YourUserModel' with your actual user model class
#             user = YourUserModel.objects.get(id=user_id)
            
#             # If using standard Django auth: user.set_password(new_password)
#             # If custom without set_password: user.password = make_password(new_password)
#             user.set_password(new_password) 
#             user.save()

#             # 5. Clear Session Variables
#             del request.session["otp"]
#             del request.session["otp_user_id"]
#             del request.session["otp_email"]
#             del request.session["otp_phone"]

#             messages.success(request, "Password updated successfully. You can now log in.")
#             return redirect('login') # Change to your login URL name

#         except YourUserModel.DoesNotExist:
#             messages.error(request, "User not found.")
#             return redirect('forgot_password')

#     # If accessed via GET directly, redirect to forgot password
#     return redirect('forgot_password')



# file end 