from django.db import models
from main.models import Notary

class Testament(models.Model):
    """Модель завещаний"""
    STATUSES = [
        ('not_canceled', 'Не отменялось'),
        ('canceled', 'Отменялось'),
        ('changed', 'Изменялось')
    ]

    testator = models.ForeignKey(
        Person, 
        on_delete=models.PROTECT,
        verbose_name='Завещатель',
        help_text='ФИО Завещателя')
    
#TODO: Сделать правильный регистрационный номер для всех нот действий и добавить модель для образов

    reg_number = models.CharField(
        max_length=50,
        )
    
    date = models.DateField(
        verbose_name='Дата удостоверения',
        help_text='Дата удостоверения'
    )

    notarius = models.ForeignKey(
        Notary,
        verbose_name='Нотариус',
        help_text='Нотариус'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        verbose_name='Сведения об отмене или изменении'
    )
