# Generated by Django 4.1.3 on 2022-11-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_sticker_alter_cleaning_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='jar',
            name='stickers',
            field=models.ManyToManyField(to='main_app.sticker'),
        ),
    ]
