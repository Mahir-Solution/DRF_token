from django.contrib import admin
from .models import Chair
@admin.register(Chair)
class ChairAdmin(admin.ModelAdmin):
    list_display = ['id','model','color','address','price']
# Register your models here.
