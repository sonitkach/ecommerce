# Generated by Django 3.1 on 2020-12-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201217_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='udername',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
