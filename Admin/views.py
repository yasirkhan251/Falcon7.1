from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product
from Bookings.models import Booking, BookingAddress
from Accounts.models import MyUser
import json
from django.views.decorators.http import require_POST
from django.db import connection, transaction
from django.contrib.auth.decorators import user_passes_test

@require_POST
def move_item_to_folder(request):
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
        target_folder_id = data.get('folder_id')
        item_type = data.get('type')

        target_folder = get_object_or_404(Category, id=target_folder_id)

        if item_type == 'product':
            # Make sure 'Product' matches your model class name
            product = get_object_or_404(Product, id=item_id)
            product.category = target_folder
            product.save()
        
        elif item_type == 'folder':
            folder = get_object_or_404(Category, id=item_id)
            if folder.id != target_folder.id:
                folder.parent = target_folder
                folder.save()

        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(f"Error moving item: {e}") # This prints the error to your terminal
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def Admin_dashboard(request):
    bookings = Booking.objects.all().order_by('-created_at') # Newest first
    bookings_count = bookings.count()
    
    bookings_pending = bookings.filter(status='pending')
    bookings_pending_count = bookings_pending.count()
    
    # Efficiently getting addresses related to these bookings
    bookings_addresses = BookingAddress.objects.filter(booking__in=bookings)
    
    clients = MyUser.objects.filter(is_admin=False)
    clientscount = clients.count()

    bookings_today = bookings.filter(created_at__date=date.today())
    bookings_today_count = bookings_today.count()

    context = {
        'bookings_count': bookings_count,
        'clientscount': clientscount,
        'bookings_pending_count': bookings_pending_count,
        'bookings_addresses': bookings_addresses,   
        'recent_bookings': bookings[:5],  # Sending the 10 latest to the table
        'clients': clients,
        'bookings_today_count': bookings_today_count,
        'all_bookings': bookings
    }
    
    return render(request, 'Admin/Admin_dashboard.html', context)
    
# Edit View
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        # Example: Updating status
        booking.status = request.POST.get('status')
        booking.save()
        return redirect('Admin_products')
    
    return render(request, 'Admin/edit_booking.html', {'booking': booking})

# Delete View
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
    return redirect('Admin_products')

def Admin_products(request, category_id=None):
    if category_id:
        current_folder = get_object_or_404(Category, id=category_id)
        # Fix: Ensure these match the related_names in your models.py
        sub_folders = current_folder.children.all().order_by('display_order')
        files = current_folder.products.all().order_by('display_order')
    else:
        current_folder = None
        sub_folders = Category.objects.filter(parent__isnull=True).order_by('display_order')
        files = []

    return render(request, 'Admin/Admin_products.html', {
        'current_folder': current_folder,
        'sub_folders': sub_folders,
        'files': files
    })

def add_folder(request):
    if request.method == "POST":
        name = request.POST.get('name')
        parent_id = request.POST.get('parent_id')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        parent = Category.objects.get(id=parent_id) if parent_id else None
        Category.objects.create(name=name, parent=parent, image=image, description=description)
        
        # FIX: Changed 'category_id' to match your admin_dashboard parameter
        if parent_id:
            return redirect('Admin_products_folder', category_id=parent_id)
    return redirect('Admin_products')

def add_product(request):
    if request.method == "POST":
        cat_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=cat_id)
        
        Product.objects.create(
            category=category,
            brand=request.POST.get('brand'),
            model_name=request.POST.get('model_name'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            image=request.FILES.get('image') # Added image support
        )
        return redirect('Admin_products_folder', category_id=cat_id)
    return redirect('Admin_products')

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        if request.FILES.get('image'):
            category.image = request.FILES.get('image')
        category.save()
        
        # FIX: Unified parameter name to category_id
        if category.parent:
            return redirect('Admin_products_folder', category_id=category.parent.id)
        return redirect('Admin_products')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.brand = request.POST.get('brand')
        product.model_name = request.POST.get('model_name')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        # FIX: Unified parameter name to category_id
        return redirect('Admin_products_folder', category_id=product.category.id)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    parent_id = category.parent.id if category.parent else None
    category.delete()
    
    if parent_id:
        return redirect('Admin_products_folder', category_id=parent_id)
    return redirect('admin_dashboard')

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category_id = product.category.id
    product.delete()
    return redirect('Admin_products_folder', category_id=category_id)

# Added the missing drag-and-drop view
def update_display_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for item in data.get('items', []):
            if item['type'] == 'folder':
                Category.objects.filter(id=item['id']).update(display_order=item['order'])
            else:
                Product.objects.filter(id=item['id']).update(display_order=item['order'])
        return JsonResponse({'status': 'success'})
    


def bookinglist(request):
    bookings = Booking.objects.all()
    booking_addresses = BookingAddress.objects.filter(booking__in=bookings)     
    context = {
        'bookings': bookings,
        'booking_addresses': booking_addresses
    }

    return render(request, 'Admin/bookinglist.html', context)


@user_passes_test(lambda u: u.is_staff)
def manual_sql_query(request):
    """
    Advanced SQL Console View:
    - Splits multiple semicolon-separated statements.
    - Executes actions (UPDATE/INSERT/DELETE) and clears them from the console.
    - Keeps SELECT queries in the console for continued viewing.
    - Detects table names for interactive grid features.
    """
    context = {
        'query': '', 
        'results': [], 
        'headers': [], 
        'error': None, 
        'table_name': '', 
        'message': None
    }
    
    if request.method == "POST":
        action = request.POST.get('action')
        raw_query = request.POST.get('sql_query', '').strip()

        # --- CASE 1: EXECUTE BUTTON CLICKED ---
        if action == "execute" and raw_query:
            try:
                # Using atomic transaction to ensure data integrity if one of many updates fails
                with transaction.atomic():
                    with connection.cursor() as cursor:
                        # Split by semicolon and remove empty lines
                        statements = [s.strip() for s in raw_query.split(';') if s.strip()]
                        
                        select_statements = []
                        action_count = 0
                        
                        for statement in statements:
                            cursor.execute(statement)
                            
                            # If it's a SELECT, we want to show results and keep the text in the box
                            if statement.upper().startswith("SELECT"):
                                select_statements.append(statement)
                                if cursor.description:
                                    context['headers'] = [col[0] for col in cursor.description]
                                    context['results'] = cursor.fetchall()
                                    
                                    # Detect table name for the "Delete" and "Edit" JS logic
                                    # Looks for the word after 'FROM'
                                    parts = statement.upper().split("FROM")
                                    if len(parts) > 1:
                                        context['table_name'] = parts[1].strip().split(" ")[0].split(";")[0]
                            else:
                                # It's an UPDATE, INSERT, or DELETE
                                action_count += 1

                        # --- CONSOLE CLEANING ---
                        # We only send SELECT queries back to the template 'query' variable.
                        # This removes the UPDATE commands so they don't run twice.
                        context['query'] = ";\n".join(select_statements)
                        if select_statements:
                            context['query'] += ";"

                        # Status Message
                        msg = f"Successfully executed {action_count} actions."
                        if select_statements:
                            msg += " Results refreshed."
                        context['message'] = msg
            
            except Exception as e:
                context['error'] = str(e)
                context['query'] = raw_query # Keep everything in the box so user can fix the error

        # --- CASE 2: DELETE ROW BUTTON CLICKED ---
        elif action == "delete_row":
            target_table = request.POST.get('target_table')
            row_id = request.POST.get('row_id')
            # We keep the current query text so the table stays visible after delete
            original_query = request.POST.get('sql_query', '') 
            
            try:
                with connection.cursor() as cursor:
                    # Execute the delete
                    cursor.execute(f"DELETE FROM {target_table} WHERE id = %s", [row_id])
                    
                    # Refresh the table immediately by re-running the SELECT query
                    statements = [s.strip() for s in original_query.split(';') if s.strip()]
                    for stmt in statements:
                        if stmt.upper().startswith("SELECT"):
                            cursor.execute(stmt)
                            context['headers'] = [col[0] for col in cursor.description]
                            context['results'] = cursor.fetchall()
                            context['query'] = stmt + ";"
                            break
                            
                context['message'] = f"Row {row_id} deleted successfully from {target_table}."
            except Exception as e:
                context['error'] = f"Delete Error: {str(e)}"
                context['query'] = original_query

    return render(request, 'Admin/sql_quarry.html', context)