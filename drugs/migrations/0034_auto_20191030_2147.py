# Generated by Django 2.2.6 on 2019-10-30 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0033_auto_20191030_1553'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='drug',
            name='compound_name',
        ),
    ]
