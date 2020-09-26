from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название компании', unique=True)
    adress = models.CharField(max_length=150, verbose_name='Адрес компании')

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'

    def __str__(self):
        return self.name

class AdditionalOffice(models.Model):
    company = models.ForeignKey(Company, related_name='additional_office', verbose_name='Компания',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Название офиса', unique=True)
    adress = models.CharField(max_length=150, verbose_name='Адрес офиса')

    class Meta:
        verbose_name = 'офис'
        verbose_name_plural = 'офисы'

    def __str__(self):
        return self.name

class Cabinet(models.Model):
    additional_office = models.ForeignKey(AdditionalOffice, related_name='cabinet',
                                          verbose_name='Офис',
                                          on_delete=models.CASCADE)
    floor = models.PositiveIntegerField(verbose_name='Этаж')
    number = models.PositiveIntegerField(verbose_name='Номер кабинета')

    class Meta:
        verbose_name = 'кабинет'
        verbose_name_plural = 'кабинеты'
        constraints = [
            models.UniqueConstraint(fields=('additional_office', 'floor', 'number'),
                                    name='unique_cabinet'),]

    def __str__(self):
        return str(self.number)



class Collaborator(models.Model):
    user = models.OneToOneField(User, related_name='user', verbose_name='Пользователь',
                                on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, related_name='cabinet', verbose_name='Кабинет',
                                on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Должность')

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self):
        return self.full_name

