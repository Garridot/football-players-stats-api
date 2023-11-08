from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
   list_display = ('email', 'is_staff')
   list_filter = ('is_staff',)
admin.site.register(User,UserAdmin)

