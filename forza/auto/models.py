import os

from django.urls import reverse
from django.db import models

class Brands(models.Model):
	brand = models.CharField(max_length=150, db_index=True, verbose_name='Бренд')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	country = models.CharField(max_length=150, verbose_name='Производитель')
	logo = models.ImageField(upload_to='logo', verbose_name='Логотип')

	def __str__(self):
		return self.brand

	def get_absolute_url(self):
		return reverse('brand', kwargs={'brand_slug': self.slug})

	# def get_absolute_image(self):
	# 	return os.path.join('/media', self.image.logo)

	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'
		ordering = ['brand']

class TypeDrive(models.Model):
	type = models.CharField(max_length=50, verbose_name='Тип привода')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = 'Привод'
		verbose_name_plural = 'Приввод'
		ordering = ['type']

class Cars(models.Model):
	brand = models.ForeignKey(Brands, on_delete=models.PROTECT, verbose_name='Бренд')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	model = models.CharField(max_length=150, verbose_name='Модель')
	year = models.PositiveSmallIntegerField(blank=True, default=True,verbose_name='Год')
	photo = models.ImageField(upload_to='cars/%Y/%m/%d', verbose_name='Фото', null=True, blank=True)
	speed = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Скорость')
	control = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Управление')
	acceleration = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Ускорение')
	start = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Старт')
	brake = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Торможение')
	Hp = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Л.с.')
	Hm = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Н/м')
	weight = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Вес')
	type_drive = models.ForeignKey(TypeDrive, on_delete=models.PROTECT, verbose_name='Тип привода')
	level = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Класс')
	price = models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Цена')

	def __str__(self):
		return self.model

	def get_absolute_url(self):
		return reverse('car', kwargs={'car_slug': self.slug})

	# def get_absolute_image(self):
	# 	return reverse('car', kwargs={'car_slug': self.slug})

	def get_absolute_image(self):
		return os.path.join('/media/logo', self.slug)

	class Meta:
		verbose_name = 'Автомобиль'
		verbose_name_plural = 'Автомобили'
		ordering = ['model']