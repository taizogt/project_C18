# Generated by Django 3.2.10 on 2023-11-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emfood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emfood',
            name='user',
            field=models.CharField(default='unknown', max_length=10),
        ),
    ]
