from django.db import models


class Notary(models.Model):
    """Модель нотариуса"""

    NOTARY_DISTRICTS = [
        ('alagir', 'Алагирский нотариальный округ'),
        ('ardon', 'Ардонский нотариальный округ'),
        ('vladik', 'Владикавказский нотариальный округ'),
        ('digora', 'Дигорский нотариальный округ'),
        ('iraf', 'Ирафский нотариальный округ'),
        ('kirov', 'Кировский нотариальный округ'),
        ('mozdok', 'Моздокский нотариальный округ г. Москвы'),
        ('pravober', 'Правобережный нотариальный округ'),
        ('prigorod', 'Пригородный нотариальный округ'),
    ]
    name = models.CharField(
        max_length=100,
        verbose_name="ФИО нотариуса",
        help_text="ФИО нотариуса")

    fed_number = models.CharField(
        verbose_name='Фед. номер',
        help_text='Фед. номер',
        blank=True,
        default='')

    reg_number = models.CharField(
        max_length=20,
        verbose_name='Регистрационный номер',
        help_text='Регистрационный номер',
        blank=True,
        default='')

    short_name = models.CharField(
        max_length=50,
        verbose_name="Краткое ФИО",
        help_text="Краткое ФИО")

    notary_district = models.CharField(
        choices=NOTARY_DISTRICTS,
        max_length=150,
        verbose_name="Нотариальный округ",
        help_text="Нотариальный округ",
        blank=True,
        default='')

    phone = models.CharField(
        max_length=20,
        verbose_name="Номер телефона",
        help_text="Номер телефона",
        blank=True,
        default='')

    mail = models.EmailField(
        verbose_name='Email',
        help_text="Email",
        blank=True,
        default='')

    class Meta:
        verbose_name = 'Нотариус'
        verbose_name_plural = 'Нотариусы'
        ordering = ['name']

    def __str__(self):
        return self.name


class InheritanceCases(models.Model):
    """Модель наследственного дела"""

    number = models.CharField(
        max_length=50,
        verbose_name='Номер н/д',
        help_text='Номер н/д')

    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия наследодателя',
        help_text='Фамилия наследодателя')

    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя наследодателя',
        help_text='Имя наследодателя')

    patronymic = models.CharField(
        max_length=50,
        verbose_name='Отчество наследодателя',
        help_text='Отчество наследодателя',
        blank=True,
        default='')

class Statement(models.Model):
    """Модель заявлений"""

    statement_type = models.CharField(

    )
 
    statement_fio = models.CharField