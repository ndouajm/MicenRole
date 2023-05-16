from django.contrib import admin
from .models import Roles

# Register your models here.

class AdminRole(admin.ModelAdmin):
    list_display = ('id', 'nom', 'date_conseil','date')

admin.site.register(Roles, AdminRole)

