from django.db import models
from main.models import Person

class InheritanceCase(models.Model):
    """Модель наследственного дела"""

    number = models.CharField(
        max_length=50,
        verbose_name='Номер н/д',
        help_text='Номер н/д')

    


class Statement(models.Model):
    """Модель заявления"""

    STATEMENT_TYPE=[
        ('otkaz','Отказ от наследства')
    ]
#TODO: Дописать виды заявлений из экспресса

    statement_type = models.CharField(
        choices=STATEMENT_TYPE,
        max_length=150,
        verbose_name='Тип заявления',
        help_text='Тип заявления'
    ) 

    applicant = models.ForeignKey(
        Person, 
        on_delete=models.PROTECT,
        verbose_name='Заявитель'
    )

    date = models.DateField(
        verbose_name='Дата заявления',
    )