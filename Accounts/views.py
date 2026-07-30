from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import MyUser
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.db.models import Q
from .otp import *

import random

def userobj(userinput):
    return MyUser.objects.filter(
        Q(phone=userinput) | Q(email=userinput)
    ).first()



def auth(request):
    """Handles Login: Phone + Password with Admin Check"""
    next_url = request.GET.get('next') or request.POST.get('next') or 'index'
    count = request.session.get("login_attempts", 0)
    if request.method == 'POST':
        userinput = request.POST.get('userinput')
        password = request.POST.get('password')
        
        try:
            # 1. Fetch user by phone to get the internal username
            user_obj = userobj(userinput)
            
            if user_obj is None:
                messages.error(request, "Phone or Email not registered.")
                return render(request, "Auth/auth.html", {
                    "next": next_url,
                    "count": count
                })
            # 2. Authenticate using the username (as required by Django internals)
            
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user is not None:
                login(request, user)
                request.session['is_admin'] = False
                # 3. Check for is_admin status
                if user.is_admin:
                    request.session['is_admin'] = True
                    # Render the specific admin template
                    return redirect('Admin_dashboard')
                
                # Standard user redirect
                return redirect(next_url)
            else:
                count += 1
                request.session["login_attempts"] = count

                messages.error(request, f"Incorrect password. Attempt {count}")                
        
        except MyUser.DoesNotExist:
            messages.error(request, "Phone number not registered.")

    return render(request, 'Auth/auth.html', {'next': next_url, "count":count})


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Auth/auth.html')

        if MyUser.objects.filter(phone=phone).exists():
            messages.error(request, "This phone number is already registered.")
            return render(request, 'Auth/auth.html')

        try:
            # We create the instance manually to avoid the Manager passing 'email'
            user = MyUser(
                username=phone,
                phone=phone,
                name=name,
                email= email
            )
            user.set_password(password) # This hashes the password correctly
            user.save() # This triggers your generate_server_id() logic
            
            login(request, user)
            messages.success(request, f"Welcome {name}! Your ID is {user.server_id}")
            return redirect('index')
            
        except Exception as e:
            print(f"Registration Error: {e}")
            messages.error(request, "An error occurred during registration.")
            return render(request, 'Auth/auth.html')
    return render(request, 'Auth/auth.html')


def forget_password(request):

    if request.method == "POST":

        user = request.POST.get("user")

        userinlist = userobj(user)

        if not userinlist:
            messages.error(request, "Phone or Email not Found.")
            return render(request, "Auth/forgot_password.html")

        if not userinlist.email:
            messages.error(request, "This account has no email address.")
            return render(request, "Auth/forgot_password.html")

        # Generate OTP only ONCE
        otp = generate_otp()

        # Store OTP in session
        request.session["otp"] = str(otp)
        request.session["otp_user_id"] = userinlist.id
        request.session["otp_email"] = userinlist.email
        request.session["otp_phone"] = userinlist.phone

        # OTP expires after 5 minutes
        request.session.set_expiry(300)

        # Send the SAME OTP to email
        send_otp(
              
            userinlist.name,
            userinlist.email,
            userinlist.phone,
            otp
        )
        
        messages.success(request, "OTP has been sent to your registered email.")
        return render(request, 'Auth/otp.html', {
            'email': userinlist.email,
            'phone': userinlist.phone
        })
    return render(request, "Auth/forgot_password.html")



def verify_otp(request):
    if request.method == "POST":
        submitted_otp = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password") 
        # session variable calling 
        session_otp = request.session.get("otp")
        user_id = request.session.get("otp_user_id")
        email = request.session.get("otp_email")
        phone = request.session.get("otp_phone")

        if not session_otp or not user_id:
            messages.error(request, "Session expired. Please request a new OTP.")
            return redirect('forgot_password') # Change to your forgot password URL name

        # 2. Validate OTP
        if submitted_otp != session_otp:
            messages.error(request, "Invalid OTP. Please try again.")
            return render(request, 'Auth/otp.html', {'email': email})

        # 3. Validate Passwords
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Auth/otp.html', {'email': email})
            
        if len(new_password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return render(request, 'Auth/otp.html', {'email': email})

        # 4. Update the Password
        try:
            # Assuming you have a way to fetch the user by ID
            # Replace 'YourUserModel' with your actual user model class
            user = MyUser.objects.get(id=user_id)
            
            # If using standard Django auth: user.set_password(new_password)
            # If custom without set_password: user.password = make_password(new_password)
            user.set_password(new_password) 
            user.save()

            # 5. Clear Session Variables
            del request.session["otp"]
            del request.session["otp_user_id"]
            del request.session["otp_email"]
            del request.session["otp_phone"]

            messages.success(request, "Password updated successfully. You can now log in.")
            return redirect('auth') # Change to your login URL name

        except MyUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('forgot_password')

    # If accessed via GET directly, redirect to forgot password
    return redirect('forgot_password')




def resend_otp(request):
    if request.method == "POST":
        user_id = request.session.get("otp_user_id")
        
        if not user_id:
            messages.error(request, "Session expired. Please enter your email/phone again.")
            return redirect('forgot_password')

        try:
            user = MyUser.objects.get(id=user_id)
            
            # Generate new OTP
            new_otp = generate_otp()
            
            # Update session and reset expiry
            request.session["otp"] = str(new_otp)
            request.session.set_expiry(300) # Reset to 5 mins
            
            # Send the email using your existing function
            send_otp(user.name, user.email, user.phone, new_otp)
            
            messages.success(request, "A new OTP has been sent to your email.")
            return render(request, 'Auth/otpverification.html', {
                'email': user.email,
                'phone': user.phone
            })
            
        except MyUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('forgot_password')
            
    return redirect('forgot_password')

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to home page after logout