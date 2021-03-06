# Generated by Django 2.2.6 on 2019-10-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0007_auto_20191025_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='activity_comment',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='drug',
            name='compound_name',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='drug',
            name='uniprot_id',
            field=models.CharField(default='-', max_length=1000),
        ),
    ]
