# Generated by Django 4.2.2 on 2023-12-24 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='state',
            new_name='state_name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='state',
        ),
    ]
