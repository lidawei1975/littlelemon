# Generated by Django 5.0.3 on 2024-03-17 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='ID',
            new_name='id',
        ),
    ]
