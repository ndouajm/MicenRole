from django.contrib import admin
from .models import Roles

# Register your models here.

class AdminRole(admin.ModelAdmin):
    list_display = ('id', 'objet', 'nom', 'date_conseil','created_at', 'etats')

admin.site.register(Roles, AdminRole)

