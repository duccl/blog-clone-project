# Generated by Django 3.0.4 on 2020-05-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0007_auto_20200526_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]