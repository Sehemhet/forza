from django.contrib import admin
from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year') #отражение полей в админке
    list_display_links = ('brand', 'model') #поля ссылка в админке
    search_fields = ('brand', 'model', 'year') #поле поиска
    list_filter = ('brand', 'model', 'year') # добавление фильтра
    prepopulated_fields = {"slug": ("brand","model","year",)}

class TypeDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'type') #отражение полей в админке
    list_display_links = ('type',) #поля ссылка в админке
    search_fields = ('type',) #поле поиска
    list_filter = ('type',) # добавление фильтра

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'country', 'logo') #отражение полей в админке
    list_display_links = ('brand', 'country') #поля ссылка в админке
    search_fields = ('brand', 'country') #поле поиска
    list_filter = ('brand', 'country') # добавление фильтра
    prepopulated_fields = {"slug": ("brand",)}

admin.site.register(Brands, BrandsAdmin)
admin.site.register(TypeDrive, TypeDriveAdmin)
admin.site.register(Cars, CarsAdmin)

