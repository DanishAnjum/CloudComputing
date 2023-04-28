# Generated by Django 4.1.5 on 2023-04-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataowner', models.CharField(default='pending', max_length=100)),
                ('filename', models.CharField(default='empty', max_length=50)),
                ('filedata', models.FileField(upload_to='static\\files')),
                ('encrypted_data', models.CharField(default='empty', max_length=500)),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
        ),
    ]
