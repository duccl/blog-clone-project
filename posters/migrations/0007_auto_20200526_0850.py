# Generated by Django 3.0.4 on 2020-05-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0006_auto_20200423_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body_text',
            field=models.TextField(default='', max_length=250),
        ),
    ]
