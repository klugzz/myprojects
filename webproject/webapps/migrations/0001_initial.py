# Generated by Django 3.2.18 on 2023-11-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('mobile', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
