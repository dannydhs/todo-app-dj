# Generated by Django 4.2.7 on 2023-12-02 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completed',
        ),
    ]
