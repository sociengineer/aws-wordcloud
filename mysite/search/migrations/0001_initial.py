# Generated by Django 3.2.9 on 2021-11-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateTimeField(max_length=250)),
                ('rating', models.IntegerField()),
                ('tokens', models.CharField(max_length=100000)),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'ordering': ('name',),
            },
        ),
    ]
