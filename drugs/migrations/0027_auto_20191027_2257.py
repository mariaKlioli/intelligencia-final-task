# Generated by Django 2.2.6 on 2019-10-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0026_drug_assay_cell_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='assay_format',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='assay_sub_type',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='assay_type',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='authors',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='chembl_id',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='compound_concetration_value',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='compound_concetration_value_unit',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='detection_technology',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
    ]