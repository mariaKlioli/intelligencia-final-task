# Generated by Django 2.2.6 on 2019-10-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0003_auto_20191025_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='compound_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='drug',
            name='uniprot_id',
            field=models.CharField(default='', max_length=1000),
        ),
    ]