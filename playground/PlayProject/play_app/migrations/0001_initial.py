# Generated by Django 4.1.7 on 2023-03-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, unique=True)),
                ('last_name', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
