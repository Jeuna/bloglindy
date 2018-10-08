import django.contrib

# Register your models here.
from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date']
    list_display_links = ['title','create_date']
    list_filter = ['create_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}

    class Meta:
       model = Blog

django.contrib.admin.site.register(Blog, BlogAdmin)