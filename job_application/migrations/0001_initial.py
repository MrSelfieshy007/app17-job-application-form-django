# Generated by Django 4.2.3 on 2023-07-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
                ('date', models.DateField(max_length=80)),
                ('occupation', models.CharField(max_length=80)),
            ],
        ),
    ]
