# Generated by Django 4.0.1 on 2022-01-28 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='name',
            new_name='school_name',
        ),
    ]
