# Generated by Django 4.1.5 on 2023-01-28 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_orders_books_orders_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='books',
            new_name='book',
        ),
    ]