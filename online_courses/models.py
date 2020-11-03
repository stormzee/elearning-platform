from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    
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
    