# Generated by Django 4.1.5 on 2023-01-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.CharField(max_length=50, verbose_name='URL')),
                ('icon', models.ImageField(upload_to='icon', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Партнеры',
                'verbose_name_plural': 'Партнеры',
                'ordering': ['name'],
            },
        ),
    ]
