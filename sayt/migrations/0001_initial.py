# Generated by Django 4.1.7 on 2023-07-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
