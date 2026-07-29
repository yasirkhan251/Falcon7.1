from django.urls import path
from .views import *    

urlpatterns = [
    path('', auth, name='auth'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('forgot_password/', forget_password, name='forgot_password'),
]