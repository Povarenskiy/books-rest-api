from django.db import models


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField('Название тега', max_length=55)
    

class Book(models.Model):
    """Модель книги"""
    rus_name = models.CharField('Русское название', max_length=255)
    eng_name = models.CharField('Английское название', max_length=255, null=True, blank=True)
    alt_name = models.CharField('Альтернативное название', max_length=255, null=True, blank=True)
    description = models.CharField('Описание', max_length=255, null=True, blank=True)

    tag = models.ManyToManyField(Tag)


class Volume(models.Model):
    """Модель тома"""
    name = models.CharField('Название', max_length=255)
    price = models.IntegerField('Стоимость')
    number = models.IntegerField('Номер')

    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Chapter(models.Model):
    """Модель главы"""
    content = models.CharField('Контент', max_length=1000)    
    number = models.IntegerField('Номер')
    
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=0)
    likes = models.IntegerField('Лайки', default=0)

