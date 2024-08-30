from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=250, blank=True, null=True, verbose_name='ФИО')
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')
    series_and_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Серия и номер паспорта')
    date_of_issue = models.CharField(max_length=11, blank=True, null=True, verbose_name='Дата выдачи')
    issued_by = models.CharField(max_length=150, blank=True, null=True, verbose_name='Кем выдан')
    birthday = models.CharField(max_length=10, blank=True, null=True, verbose_name='Дата рождения')
    department_code = models.CharField(max_length=8, blank=True, null=True, verbose_name='Код подразделения')
    registration_address = models.CharField(max_length=150, blank=True, null=True, verbose_name='Адрес регистрации (прописки)')

    class Meta:
        db_table = 'user'
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username