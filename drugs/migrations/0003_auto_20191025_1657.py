# Generated by Django 2.2.6 on 2019-10-25 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0002_auto_20191025_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='authors',
            new_name='uniprot_id',
        ),
    ]