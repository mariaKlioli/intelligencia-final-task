# Generated by Django 2.2.6 on 2019-10-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0014_auto_20191025_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='annotation_comments',
            field=models.CharField(default='-', max_length=1000, null=True),
        ),
    ]