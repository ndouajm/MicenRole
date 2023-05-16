
from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('create', roleCreate, name="create"),
    path('detail/<int:role_id>/', role_detail, name='role_detail'),
    path('print/', print_document, name='print_document'),
]
