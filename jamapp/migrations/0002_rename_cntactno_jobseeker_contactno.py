# Generated by Django 4.1 on 2022-08-29 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobseeker',
            old_name='cntactno',
            new_name='contactno',
        ),
    ]
