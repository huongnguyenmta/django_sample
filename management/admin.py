from django.contrib import admin
from .models import MyUser, Book, Author

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    ordering = ["role"]
    search_fields = ["email"]
    list_display = ("email", "role")
    fields = ("email", "password", "role")
