from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media")
    
    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=50)
    cat_thumbnail = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=225)
    Description = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True)
    no_of_comments = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='media')
    categories = models.ManyToManyField(Category)
    creator = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField(default=None)
    
    def __str__(self):
        return self.title


# Now we are adding a comment system to our app
# 1st, create a model for the comment system(thus, where the comments will be stored at the backend)
# And then create a file (forms.py==> this is a form file in which you will show all the fields you want to take user inpt)
# that will be used to take the comments on the frontend from users
# After creating the form, you can display the form on the frontend 
    @property
    def get_comments(self):
        return self.comments.all().order_by('-time_created')
    
    # comments = property(get_comments)

class Comment(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    