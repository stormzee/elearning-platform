# Generated by Django 3.1.2 on 2020-11-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(upload_to='media'),
        ),
    ]
