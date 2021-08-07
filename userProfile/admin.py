from django.contrib import admin
from .models import UserProfile

class CustomUserAdmin(admin.ModelAdmin):
    model = UserProfile
    
admin.site.register(UserProfile, CustomUserAdmin)