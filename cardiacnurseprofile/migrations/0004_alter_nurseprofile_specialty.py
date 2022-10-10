# Generated by Django 3.2.15 on 2022-10-10 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardiacnurseprofile', '0003_auto_20221010_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurseprofile',
            name='specialty',
            field=models.CharField(blank=True, choices=[(1, 'Ischemic Heart Disease'), (2, 'Heart Failure'), (3, 'Coronary Care'), (4, 'Arrythmia'), (5, 'Congenital Heart Disease'), (6, 'Other')], max_length=50, null=True),
        ),
    ]
