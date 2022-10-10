# Generated by Django 3.2.15 on 2022-10-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardiacnurseprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='specialty',
            field=models.CharField(blank=True, choices=[(1, 'IHD'), (2, 'HF'), (3, 'CCU')], max_length=50, null=True),
        ),
    ]
