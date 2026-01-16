from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 1. The Root (Mobile, Laptop, etc.)
    # Maps to universal_view(slug=None, product_id=None)
    path('', universal_view, name='service_root'),
    
    # 2. AJAX Order Update (Specific paths should ALWAYS go before variable paths like slugs)
    path('update-order/', update_display_order, name='update_display_order'),

    # 3. The final service page for a product
    # Maps to universal_view(slug=None, product_id=YOUR_ID)
    path('service-details/<int:product_id>/', universal_view, name='service_detail'),

    # 4. Any subfolder (Xiaomi, Poco, etc.)
    # Maps to universal_view(slug=YOUR_SLUG, product_id=None)
    # WARNING: This catches almost everything, so keep it at the bottom.
    path('<slug:slug>/', universal_view, name='folder_detail'),
]



#    path('category/<slug:slug>/', category_detail, name='category_detail'),
# This name must match the 'category_detail' used in the template

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)