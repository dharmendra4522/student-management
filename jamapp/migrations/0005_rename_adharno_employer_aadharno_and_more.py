# Generated by Django 4.1 on 2022-08-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0004_enquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='adharno',
            new_name='aadharno',
        ),
        migrations.RenameField(
            model_name='employer',
            old_name='regdat',
            new_name='regdate',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='enquriytext',
            new_name='enquirytext',
        ),
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='emailaddress',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='userid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
