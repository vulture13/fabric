# Generated by Django 3.2.6 on 2022-09-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
