# Generated by Django 4.2.14 on 2024-07-22 02:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.MinLengthValidator(11)])),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
