from django.contrib import admin
from application.models import pro

# Register your models here.
@admin.register(pro)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name','price','desc','img')