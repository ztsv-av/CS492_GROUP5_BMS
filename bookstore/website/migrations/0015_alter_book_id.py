# Generated by Django 4.1.6 on 2023-02-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_rename_num_available_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Book ID'),
        ),
    ]
