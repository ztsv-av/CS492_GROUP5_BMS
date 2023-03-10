# Generated by Django 4.1.6 on 2023-02-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_rename_books_order_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='MfgInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Book Title')),
                ('author', models.CharField(max_length=100, verbose_name='Book Author')),
                ('genre', models.CharField(max_length=100, verbose_name='Book Genre/s')),
                ('available', models.BooleanField(verbose_name='Book Available')),
                ('image', models.CharField(max_length=100, verbose_name='Book Image Path')),
                ('price', models.CharField(max_length=100, verbose_name='Book Price')),
                ('qty_available', models.CharField(blank=True, max_length=10, null=True, verbose_name='Qty in Inventory')),
            ],
        ),
    ]
