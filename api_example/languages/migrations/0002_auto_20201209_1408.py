# Generated by Django 3.1.4 on 2020-12-09 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='paradign',
            new_name='paradigm',
        ),
    ]
