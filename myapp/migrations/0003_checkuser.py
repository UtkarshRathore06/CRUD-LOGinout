# Generated by Django 3.1.7 on 2021-04-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210424_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckUser',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
