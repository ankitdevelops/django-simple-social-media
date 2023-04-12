from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "email", "joined", "last_login"]
    list_filter = ["username", "email"]
    date_hierarchy = "joined"
