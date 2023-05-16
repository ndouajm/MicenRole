
from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('create', roleCreate, name="create"),
    path('detail/<int:role_id>/', role_detail, name='role_detail'),
    path('update/<int:role_id>/', roleUpdate, name='update'),
    path('delete/<int:role_id>/', delete, name='delete'),
    path('confirm_delete/', confirm_delete, name='confirm_delete'),
    path('print/<int:role_id>/', print_document, name='print_document'),
]
