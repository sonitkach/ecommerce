# Generated by Django 3.1 on 2020-12-12 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201207_1829'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderedItem',
            new_name='OrderItem',
        ),
    ]
