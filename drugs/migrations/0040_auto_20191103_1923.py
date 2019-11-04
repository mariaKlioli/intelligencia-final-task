# Generated by Django 2.2.6 on 2019-11-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0039_auto_20191103_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='target',
        ),
        migrations.AddField(
            model_name='compound',
            name='target',
            field=models.ManyToManyField(to='drugs.Target'),
        ),
    ]
