from django.db import models
from main.models import Person, Notary

class InheritanceCase(models.Model):
    """Модель наследственного дела"""

    case_number = models.CharField(
        max_length=50,
        verbose_name='Номер н/д',
        help_text='Номер н/д')

    deceased = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name='Наследодатель'
    )

    notary = models.ForeignKey(
        Notary,
        on_delete=models.PROTECT,
        verbose_name='Нотариус'
    )

    opening_date = models.DateField(
        verbose_name='Дата открытия н/д',
        help_text='Дата открытия н/д'
    )

    closing_date = models.DateField(
        verbose_name='Дата закрытия н/д',
        help_text='Дата закрытия н/д'
    )
    
        # Связь с завещанием (если есть)
    testament = models.ForeignKey(
        'testaments.Testament',
        on_delete=models.SET_NULL,
        verbose_name='Завещание',
        null=True,
        blank=True,
        related_name='linked_inheritance_cases'
    )


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