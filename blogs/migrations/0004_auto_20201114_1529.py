# Generated by Django 3.0 on 2020-11-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20201114_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
