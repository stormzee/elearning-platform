from django.shortcuts import render
from .models import Course, Category, Author
# Create your views here.

def index(request):
    return render(request, 'index.html')

def courses(request):
    category_list = Category.objects.all()
    context = {
        'category_list':category_list,
    }


    return render(request, 'courses.html', context)

def maths(request):
    maths_courses = Course.objects.filter(categories__title = 'Mathematics')
    context = {
        'maths_courses':maths_courses,
    }
    return render(request, 'maths.html', context)