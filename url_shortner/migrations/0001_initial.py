# Generated by Django 3.2 on 2022-03-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=512)),
                ('shortened_url', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
