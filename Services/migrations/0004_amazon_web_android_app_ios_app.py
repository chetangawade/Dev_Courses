# Generated by Django 4.0.3 on 2022-05-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='amazon_Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('language_info', models.CharField(max_length=500)),
                ('reference_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='android_App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('language_info', models.CharField(max_length=500)),
                ('reference_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ios_App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('language_info', models.CharField(max_length=500)),
                ('reference_link', models.CharField(max_length=100)),
            ],
        ),
    ]