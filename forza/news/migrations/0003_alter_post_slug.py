# Generated by Django 4.1.5 on 2023-01-28 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]
