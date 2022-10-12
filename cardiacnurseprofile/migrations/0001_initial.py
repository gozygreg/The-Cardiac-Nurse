# Generated by Django 3.2.15 on 2022-10-10 21:03

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('specialty',),
            },
        ),
        migrations.CreateModel(
            name='NurseProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('nurse_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('status', models.IntegerField()),
                ('year_qualified', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cardiacnurseprofile.specialty')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]