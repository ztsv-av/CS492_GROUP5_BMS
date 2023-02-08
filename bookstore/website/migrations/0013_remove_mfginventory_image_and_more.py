# Generated by Django 4.1.6 on 2023-02-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mfginventory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='mfginventory',
            name='qty_available',
        ),
        migrations.AddField(
            model_name='mfginventory',
            name='quantity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Quantity in Inventory'),
        ),
    ]
