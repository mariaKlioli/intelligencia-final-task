# Generated by Django 2.2.6 on 2019-11-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0045_auto_20191104_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='authors',
            field=models.CharField(default='', max_length=25500, null=True),
        ),
    ]
