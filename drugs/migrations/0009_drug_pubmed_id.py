# Generated by Django 2.2.6 on 2019-10-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0008_auto_20191025_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='pubmed_id',
            field=models.CharField(default='-', max_length=1000),
        ),
    ]