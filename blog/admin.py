from django.contrib import admin
from .models import *





@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_time' , 'description', 'active')
    search_fields = ['title',]
    date_hierarchy = 'created_time'
    ordering = ['-created_time']
