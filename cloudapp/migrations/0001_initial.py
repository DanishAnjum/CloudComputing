# Generated by Django 4.1.5 on 2023-04-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dataowner', models.CharField(max_length=100)),
                ('Datauser', models.CharField(max_length=100)),
                ('Filename', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('key', models.CharField(default='empty', max_length=100)),
                ('mykey', models.CharField(default='empty', max_length=100)),
            ],
        ),
    ]
