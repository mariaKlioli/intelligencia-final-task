# Generated by Django 2.2.6 on 2019-10-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0016_auto_20191025_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='compound_name',
            field=models.CharField(default='-', max_length=100, null=True, unique=True),
        ),
    ]
