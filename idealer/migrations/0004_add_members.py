# Generated by Django 2.2 on 2021-04-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idealer', '0003_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='members',
            field=models.ManyToManyField(related_name='add', to='idealer.User'),
        ),
    ]
