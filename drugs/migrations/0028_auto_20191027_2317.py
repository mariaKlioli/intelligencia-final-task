# Generated by Django 2.2.6 on 2019-10-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0027_auto_20191027_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='endpoint_actionmode',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='endpoint_standard_relation',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='endpoint_standard_type',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='endpoint_standard_units',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='endpoint_standard_value',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='gene_name',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='inhibitor_type',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='max_phase',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='mutation_info',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='protein_class',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='pubmed_id',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='resource_uri',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='target_organism',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='target_pref_name',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='wildtype_or_mutant',
            field=models.CharField(default='-', max_length=25500, null=True),
        ),
    ]
