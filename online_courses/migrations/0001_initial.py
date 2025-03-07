# Generated by Django 3.1.2 on 2020-11-02 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('Description', models.TextField()),
                ('Date_created', models.DateTimeField(auto_now_add=True)),
                ('no_of_comments', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(upload_to='media')),
                ('categories', models.ManyToManyField(to='online_courses.Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_courses.author')),
            ],
        ),
    ]
