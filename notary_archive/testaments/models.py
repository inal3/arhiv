from django.db import models
from main.models import Notary, Person

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
        help_text='ФИО Завещателя',
        related_name='testaments_as_testator')
    
#TODO: Сделать правильный регистрационный номер для всех нот действий и добавить модель для образов

    reg_number = models.CharField(
        max_length=50,
        verbose_name='Регистрационный номер',
        help_text='Регистрационный номер завещания'
    )
    
    date = models.DateField(
        verbose_name='Дата удостоверения',
        help_text='Дата удостоверения'
    )

    notarius = models.ForeignKey(
        Notary,
        on_delete=models.PROTECT,
        verbose_name='Нотариус',
        help_text='Нотариус'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        verbose_name='Сведения об отмене или изменении'
    )

    # Наследники
    heirs = models.ManyToManyField(
        Person,
        verbose_name='Наследники',
        related_name='testaments_as_heir',
        blank=True
    )
    
    # Связь с наследственным делом (если есть)
    inheritance_case = models.ForeignKey(
        'inheritance_cases.InheritanceCase',
        on_delete=models.SET_NULL,
        verbose_name='Связанное наследственное дело',
        null=True,
        blank=True,
        related_name='testaments'
    )

    class Meta:
        verbose_name = 'Завещание'
        verbose_name_plural = 'Завещания'
        ordering = ['-date']

    def __str__(self):
        return f"Завещание №{self.reg_number} от {self.date}"
    
    @property
    def main_image(self):
        """Основной образ завещания"""
        return self.images.filter(document_type='testament').first()
    
    @property
    def all_images(self):
        """Все образы, связанные с этим завещанием"""
        return self.images.all()
    
    @property
    def heirs_count(self):
        return self.heirs.count()
    
    