from django.contrib import admin

from .models import Category, Author, Course
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Course)