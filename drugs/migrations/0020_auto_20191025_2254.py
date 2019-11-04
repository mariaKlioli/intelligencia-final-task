# Generated by Django 2.2.6 on 2019-10-25 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0019_auto_20191025_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='activity_comment',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='annotated',
            field=models.CharField(default='-', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='annotation_comments',
            field=models.CharField(default='-', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='uniprot_id',
            field=models.CharField(default='-', max_length=1000, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='drug',
            unique_together=set(),
        ),
    ]