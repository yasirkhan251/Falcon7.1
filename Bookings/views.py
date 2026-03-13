from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from Admin.models import Category, Product
from services.models import ServiceCategory, ServiceProduct 
from .models import Booking, BookingAddress
from datetime import datetime
# Create your views here.


@login_required
def bookings_view(request, product, service):
    if request.method == 'POST':
        # 1. Capture Booking Data into temporary variables
        service_type = request.POST.get('service_type_val') 
        service_name = request.POST.get('service_name_val') 
        model_device = request.POST.get('model_val')
        purpose = request.POST.get('purpose_val')
        phone = request.POST.get('phone')
        booking_date = request.POST.get('booking_date')
        # Hint: You might also want to capture the 'booking_hour' we set up in the HTML!
        # booking_hour = request.POST.get('booking_hour')
        
        description = request.POST.get('description')
        
        # 2. Capture Address Data safely using .get(key, '').strip() to remove extra spaces
        house_no = request.POST.get('house_no', '').strip()
        
        building = request.POST.get('building_name', '').strip()
        street = request.POST.get('street', '').strip()
        city = request.POST.get('city', '').strip()
        state = request.POST.get('state', '').strip()
        pincode = request.POST.get('pincode', '').strip()
        landmark = request.POST.get('landmark', '').strip()
        print(house_no, building, street, city, state, pincode, landmark)
        # --- ADDRESS MERGE LOGIC ---
        # Put the parts in a list, but only if they actually contain text
        address_parts = []
        if house_no:
            address_parts.append(house_no)
        if building:
            address_parts.append(building)
        if street:
            address_parts.append(street)
            
        # Join them together with a comma and a space
        # Result example: "Flat 402, Prestige Heights, 12th Main Road"
        merged_street = ", ".join(address_parts)
        # ---------------------------

        # Basic Validation
        if not all([booking_date, merged_street, city, pincode]):
            messages.error(request, "Please fill in all required fields marked with *")
            return redirect(request.path)

        try:
            # 3. Use an atomic transaction to save to both tables
            with transaction.atomic():
                # Save Primary Booking Table
                new_booking = Booking.objects.create(
                    user=request.user,
                    service_type=service_type,
                    service_name=service_name,
                    model=model_device,
                    purpose=purpose,
                    description=description,
                    phone=phone,
                    booking_date=booking_date
                    # booking_hour=booking_hour # Uncomment if you added this to your model
                )

                # Save Linked Address Table
                BookingAddress.objects.create(
                    booking=new_booking,
                    street=merged_street,  # <-- Pass the newly merged string here
                    landmark=landmark,
                    city=city,
                    state=state,
                    pincode=pincode
                )

            messages.success(request, "Service booked successfully! Our team will contact you soon.")
            return redirect("booking_success", booking_id=new_booking.id)

        except Exception as e:
            print(f"Booking Error: {e}")
            messages.error(request, "An error occurred while saving your booking. Please try again.")
            
    # Assuming these context variables are defined earlier in your actual view
    context = {
        'type': type,
        'company': company,
        'model': model,
        'purposes': purposes
    }
    
    return render(request, 'Bookings/bookings.html', context)
@login_required
def booking_success(request, booking_id):
    booking = Booking.objects.select_related().get(id=booking_id)
    address = BookingAddress.objects.get(booking=booking)

    context = {
        "booking": booking,
        "address": address,
    }
    return render(request, "Bookings/booking_success.html", context)


@login_required
def booking_menu(request, product, service):
    # 1. Fetch the Product and Category Path (Your existing logic)
    product_obj = get_object_or_404(
        Product.objects.select_related('category__parent__parent'), 
        sku=product
    )
    category_path = product_obj.category.get_path_list()

    if request.method == 'POST':
        # 2. Extract Timing Data
        date_val = request.POST.get('booking_date')
        hour_val = request.POST.get('booking_hour') # Coming as 10, 14, 20 etc. from JS
        
        # 3. Extract Address Data Safely (.strip() removes extra spaces)
        house_no = request.POST.get('house_no', '').strip()
        building = request.POST.get('building_name', '').strip()
        street = request.POST.get('street', '').strip()
        city = request.POST.get('city', '').strip()
        pincode = request.POST.get('pincode', '').strip()
        landmark = request.POST.get('landmark', '').strip()

        # --- ADDRESS MERGE LOGIC ---
        # Add parts to a list only if they are not empty
        address_parts = []
        if house_no:
            address_parts.append(house_no)
        if building:
            address_parts.append(building)
        if street:
            address_parts.append(street)
            
        # Join them together beautifully: "Flat 402, Prestige Heights, 12th Main"
        merged_street = ", ".join(address_parts)
        # ---------------------------

        # Prevent crash if user forgets to click a time slot
        if not hour_val:
            messages.error(request, "Please select an appointment time slot.")
            return redirect(request.path)

        try:
            # Combine into Python datetime
            combined_dt = datetime.strptime(f"{date_val} {hour_val}:00", '%Y-%m-%d %H:%M')
            
            # 4. Use Atomic Transaction to save both models together
            with transaction.atomic():
                # Create the Main Booking
                booking = Booking.objects.create(
                    user=request.user,
                    service_type=category_path[0].name, # e.g., "Mobile"
                    service_name=product_obj.brand,     # e.g., "OPPO"
                    model=product_obj.model_name,       # e.g., "A6 Pro 5G"
                    purpose=service,                    # e.g., "Speaker"
                    description=request.POST.get('description'),
                    phone=request.POST.get('phone'),
                    booking_date=combined_dt
                )

                # Create the Booking Address using the merged string
                BookingAddress.objects.create(
                    booking=booking,
                    street=merged_street,               # <-- Pushing the merged address here!
                    landmark=landmark,
                    city=city,
                    pincode=pincode,
                    state="Karnataka" 
                )

            messages.success(request, f"Booking confirmed! Order ID: {booking.order_id}")
            return redirect('booking_success', token=booking.token) 

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    # Context for the GET request
    context = {
        'sku_str': product,
        'service': service,
        'product': product_obj,
        'category_path': category_path 
    }

    return render(request, 'Bookings/bookings.html', context)
def booking_success(request, token):
    # Fetch the booking using the unique token
    # Use select_related to get the address in the same query
    booking = get_object_or_404(Booking.objects.select_related('address'), token=token)
    
    return render(request, 'Bookings/success.html', {'booking': booking})



@login_required
def my_bookings(request):
    # Fetch bookings for the logged-in user
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'bookings': bookings,
    }
    return render(request, 'Bookings/my_bookings.html', context)