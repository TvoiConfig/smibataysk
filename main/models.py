from django.db import models
import os
from django.contrib.auth.models import User
from django.conf import settings

class Products(models.Model):

    CHOICE_TYPE = (
        ('about', 'О нас'),
        ('sponsor', 'Реклама'),
        ('news', 'Новость'),
        ('archive', 'Архивировано')
    )

    name = models.CharField(max_length=50, verbose_name="Имя")
    type = models.CharField(max_length=50, choices=CHOICE_TYPE, default='news', verbose_name="Тип")
    character = models.TextField(max_length=100, verbose_name="Описание")
    image = models.ImageField(null=False, blank=False, upload_to="image/")
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        
        verbose_name = 'Новость'
        verbose_name_plural = 'список новостей'
        

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
class record(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='ФИО')
    number = models.CharField(max_length=15, verbose_name='Номер телефона')
    message = models.CharField(max_length=150, verbose_name='Сообщение')
    timeposted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
#        managed = False
        db_table = 'record'
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'
        
    def __str__(self):
        return self.message
    
class Stream(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название трансляции')
    character = models.TextField(max_length=100, verbose_name='Описание трансляции')
    video = models.FileField(blank=False, verbose_name='Трансляция', upload_to="video/")
    likes = models.PositiveIntegerField(default=0)
    
    class Meta: 
        db_table = 'stream'
        verbose_name = 'Трансляция'
        verbose_name_plural = 'Трансляции'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.video:
            if os.path.isfile(self.video.path):
                os.remove(self.video.path)
        super().delete(*args, **kwargs)
        


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')