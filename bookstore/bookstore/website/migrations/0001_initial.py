# Generated by Django 4.1.5 on 2023-01-28 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Book Title')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('author', models.CharField(max_length=100, verbose_name='Book Author')),
                ('genre', models.CharField(max_length=100, verbose_name='Book Genre/s')),
                ('numPages', models.CharField(max_length=100, verbose_name='Book Number of Pages')),
                ('availabe', models.BooleanField(verbose_name='Book Available')),
                ('image', models.CharField(max_length=100, verbose_name='Book Image Path')),
                ('price', models.CharField(max_length=100, verbose_name='Book Price')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='User First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='User Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('password', models.CharField(max_length=100, verbose_name='User Password')),
                ('address', models.CharField(max_length=300, verbose_name='User Address')),
                ('zip_code', models.CharField(max_length=15, verbose_name='User Zip Code')),
                ('phone', models.CharField(max_length=15, verbose_name='User Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Order Date')),
                ('successful', models.BooleanField(verbose_name='Order Successful')),
                ('bookID', models.ManyToManyField(blank=True, to='website.books')),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.users')),
            ],
        ),
    ]
