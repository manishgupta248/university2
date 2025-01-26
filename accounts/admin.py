from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()  # Get the User model

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Fields to display in the admin list
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Fields for searching users