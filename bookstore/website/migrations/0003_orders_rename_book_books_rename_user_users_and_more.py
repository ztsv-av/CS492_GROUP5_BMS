# Generated by Django 4.1.5 on 2023-01-28 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_books_book_rename_orders_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Order Date')),
                ('successful', models.BooleanField(verbose_name='Order Successful')),
            ],
        ),
        migrations.RenameModel(
            old_name='Book',
            new_name='Books',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='orders',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.books'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.users'),
        ),
    ]
