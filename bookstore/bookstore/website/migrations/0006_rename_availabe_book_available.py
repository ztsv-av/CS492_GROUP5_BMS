# Generated by Django 4.1.5 on 2023-01-28 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_books_book_rename_orders_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='availabe',
            new_name='available',
        ),
    ]