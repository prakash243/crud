# Generated by Django 2.2.1 on 2019-10-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
