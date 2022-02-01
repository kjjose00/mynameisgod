from django.contrib import admin
from .models import User

# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','password','is_active','staff','admin']