# Generated by Django 4.1.5 on 2023-01-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]