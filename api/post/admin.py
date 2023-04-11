from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = ["title", "total_likes", "author", "created_at"]
    # list_filter = ["username", "email"]
    # date_hierarchy = "joined"
    # readonly_fields = ("password", "username")
