# Generated by Django 2.2.6 on 2019-10-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='authors',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='drug',
            name='compound_name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
