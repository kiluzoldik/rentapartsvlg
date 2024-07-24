from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Places(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    url = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL адрес')
    image = models.ImageField(upload_to='places_images', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(default='Все места',
                                 to=Categories,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'place'
        verbose_name = 'место'
        verbose_name_plural = 'места'