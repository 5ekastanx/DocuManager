from typing import Iterable
from django.db import models
from apps.accounts.models import CustomUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True



class Folder(BaseModel):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, создавший папку'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название папки',
        help_text='Название папки'
    )
    description = models.TextField(
        default='',
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Описание папки (необязательно)'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна',
        help_text='Активна ли папка'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'
        ordering = ['created_at']


class Document(BaseModel):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        verbose_name='Пользователь', 
        help_text='Пользователь, загрузивший документ'
    )
    name = models.CharField(
        max_length=200, 
        default='', 
        verbose_name='Название документа', 
        help_text='Название загруженного документа'
    )
    file = models.FileField(
        upload_to='documents/%Y/%m/%d', 
        verbose_name='Файл', 
        help_text='Загруженный файл'
    )
    description = models.TextField(
        default='', 
        blank=True, 
        null=True,
        verbose_name='Описание', 
        help_text='Описание документа (необязательно)'
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name='Активен', 
        help_text='Активен ли документ'
    )

    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        verbose_name='Папка',
        help_text='Папка, в которую загружен документ'
    )

    extension = models.CharField(
        max_length=10, 
        null=True, 
        blank=True, 
        verbose_name='Расширение файла', 
        help_text='Расширение загруженного файла'
    )
    size = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        verbose_name='Размер файла', 
        help_text='Размер файла в байтах'
    )
    access = models.ManyToManyField(
        CustomUser,
        blank=True,
        related_name='document_access_users',
        verbose_name='Доступ',
        help_text='Кому доступен документ'
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        self.extension = self.file.name.split('.')[-1]
        self.size = self.file.size
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['created_at']




