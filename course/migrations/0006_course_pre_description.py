# Generated by Django 3.2 on 2021-06-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20210614_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pre_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
