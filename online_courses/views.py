from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Category, Author
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import login, logout, authenticate
from .forms import CommentForm
from subscription.models import Subscriber
# Create your views here.

def index(request):
    if request.method == 'POST':
        # grab the email from the form email field
        email = request.POST['email']
        # create an instance of the subcriber model
        new_subscriber = Subscriber()
        # get the email of the new subscriber by using dot notation( new_subscriber.email) and assign the grabbed email to it
        new_subscriber.email = email
        # save it in the db
        new_subscriber.save()
    return render(request, 'index.html')

def categories(request):
    category_list = Category.objects.all()
    context = {
        'category_list':category_list,
    }
    return render(request, 'categories.html', context)

def maths(request):
    maths_courses = Course.objects.filter(categories__title = 'Mathematics')
    context = {
        'maths_courses':maths_courses,
    }
    return render(request, 'maths.html', context)

def english(request):
    english_courses = Course.objects.filter(categories__title = 'English')
    context = {
        'english_courses':english_courses,
    }
    return render(request, 'english.html', context)


def register(request):
    if request.method =='POST':
        # create a user creation form and put the data from the form into it.
        form = UserCreationForm(request.POST)
        # if the form input is valid, let's save the user by saving the data in the form
        if form.is_valid():
            user = form.save()
            # after saving the user(creating a new user), login the user.
            username = form.cleaned_data.get('username')
            login(request, user)
        return redirect('index')
        # else:
        #     for error in form.error_messages:
        #         # error messages is a dictionary
        #         # so we have to pass the key for the actual message to be displayed
        #         print(form.error_messages[error])
    # create new form to avoid resubmission of form 
    # or to get a new form on the template for user to fill.
    # if request is POST on the register.html==> take data and create a new user with it
    # else if there is a GET (no post request), create a new form on the page for the user
    # this is what happens the 1st time you visit the register.html page cuz there is no POST request
    form = UserCreationForm        
    return render(request, 'register.html', context = {'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')

def user_login(request):
    if request.method == 'POST':
        # if the request is a post request, 
        # take the data from the form. username= request.post['username'], password=request.post['pass']
        # authenticate the credentials to verify that the user exists
        # if user exists, do login. thus login(request, user)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def course(request, course_id):
    try:
        course = get_object_or_404(Course, id = course_id)
    except Course.DoesNotExist:
        raise Http404("Course doesnt exist")
# we are implementing our comment system here
# 1st create an instance of the comment form and populate it with the iput data from the user
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # assign the user and the course of that particular comment
            form.instance.user = request.user
            form.instance.course = course
            form.save()        
        return redirect('course', course_id=course_id)
    return render(request, 'course.html', context={'course':course, 'form':form})
    
