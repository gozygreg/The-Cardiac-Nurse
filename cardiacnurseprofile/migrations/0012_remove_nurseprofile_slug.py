# Generated by Django 3.2.15 on 2022-10-14 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardiacnurseprofile', '0011_alter_nurseprofile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurseprofile',
            name='slug',
        ),
    ]
