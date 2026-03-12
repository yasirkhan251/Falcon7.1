from django.shortcuts import render,redirect,get_object_or_404
from Admin.models import *
from django.http import JsonResponse


# Create your views here.


def index(request):
    # --- HANDLE FORM SUBMISSION ---
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        category_id = request.POST.get('category_id')

        # If user selected a specific model (Final Level)
        if product_id:
            # Matches: name='service_detail' -> path('service-details/<int:product_id>/'...)
            return redirect('service_detail', product_id=product_id)
        
        # If user only selected a Category/Brand (Folder Level)
        elif category_id:
            category = get_object_or_404(Category, id=category_id)
            # Matches: name='folder_detail' -> path('<slug:slug>/'...)
            return redirect('folder_detail', slug=category.slug)

    # --- INITIAL GET LOGIC (Categories for Dropdown) ---
    desired_order = ["MOBILE", "LAPTOP", "TABLET", "PC / DESKTOP", "CCTV"]
    root_categories = Category.objects.filter(parent__isnull=True, is_active=True)
    
    order_mapping = {name: i for i, name in enumerate(desired_order)}
    sorted_categories = sorted(
        root_categories,
        key=lambda cat: order_mapping.get(cat.name.upper(), len(desired_order))
    )
    
    return render(request, 'Falcon/index.html', {'categories': sorted_categories})



def get_subcategories(request):
    parent_id = request.GET.get('parent_id')
    
    # 1. Fetch Sub-folders (Brands/Series) matching Scenario B logic
    sub_folders = Category.objects.filter(parent_id=parent_id, is_active=True)
    
    # 2. Fetch Products tied to this category (The final level)
    products = Product.objects.filter(category_id=parent_id, is_active=True)
    
    # Combine data for the dropdown
    data = []
    
    # Add folders (Next level of dropdown)
    for folder in sub_folders:
        data.append({'id': folder.id, 'name': folder.name, 'type': 'folder'})
        
    # Add products (The final selection)
    for product in products:
        data.append({'id': product.id, 'name': product.name, 'type': 'product'})
        
    return JsonResponse(data, safe=False)



def about(request):
    return render(request, 'Falcon/about.html')

def contact(request):
    return render(request, 'Falcon/contact.html')
def team(request):
    return render(request, 'Falcon/team.html')
def pricing(request):
    return render(request, 'Falcon/pricing.html')
def privacy(request):
    return render(request, 'Falcon/privacy.html')
def terms(request):
    return render(request, 'Falcon/terms.html')
def maintenance(request):
    return render(request, 'Falcon/maintenance.html')
def comingsoon(request):
    return render(request, 'Falcon/coming-soon.html')
def search(request):
    return render(request, 'Falcon/search.html')
def blog(request):
    return render(request, 'Falcon/blog.html')
def error(request):
    return render(request, 'Falcon/404.html')
def faq(request):
    return render(request, 'Falcon/faq.html')
def service1(request):
    return render(request, 'Falcon/service1.html')




def elements(request):
    return render(request, 'elements.html')     



def appointment(request):
    return render(request, 'appointment.html')
def department(request):
    return render(request, 'department.html')
def departmentsingle(request):
    return render(request, 'department-single.html')
def doctor(request):
    return render(request, 'doctor.html')
def doctorsingle(request):
    return render(request, 'doctor-single.html')

def gallery(request):
    return render(request, 'gallery.html')
def testimonial(request):
    return render(request, 'testimonial.html')


