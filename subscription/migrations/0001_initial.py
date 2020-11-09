# Generated by Django 3.1.2 on 2020-11-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]