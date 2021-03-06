# Generated by Django 4.0.3 on 2022-03-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('National_ID', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='National ID care Numner')),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name of the owner')),
                ('phone_number', models.CharField(max_length=11)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Manwoman')], max_length=7)),
                ('citizen_of', models.CharField(max_length=5, verbose_name='selete conutry')),
                ('address_of_owner', models.CharField(max_length=100, verbose_name='address of the owner')),
            ],
            options={
                'verbose_name': 'vehicle owner',
                'verbose_name_plural': 's',
            },
        ),
    ]
