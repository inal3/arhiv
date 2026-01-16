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
        max_length=50,
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


class Person(models.Model):
    last_name=models.CharField(
        max_length=100,
        verbose_name='Фамилия',
        help_text='Фамилия физического лица'
    )

    name=models.CharField(
        max_length=100,
        verbose_name='Имя',
        help_text='Имя физического лица'
    )

    patronymic=models.CharField(
        max_length=100,
        verbose_name='Отчество',
        help_text='Отчество физического лица',
        blank=True,
        default=''
    )

    birth_date=models.DateField(
        verbose_name='Дата рождения',
        help_text='Дата рождения',
        null=True,
        blank=True
    )

    death_date=models.DateField(
        verbose_name='Дата смерти',
        help_text='Дата смерти(для наследодателей)',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Физическое лицо',
        verbose_name_plural = 'Физические лица',
        ordering = ['last_name', 'name', 'patronymic'],
        indexes = [
            models.Index(fields=['last_name', 'name']),
        ]

    def __str__(self):
        if self.patronymic:
            return f"{self.last_name} {self.name} {self.patronymic}"
        return f"{self.last_name} {self.name}"
    
    @property
    def full_name(self):
        """Полное ФИО"""
        parts = [self.last_name, self.name]
        if self.patronymic:
            parts.append(self.patronymic)
        return ' '.join(parts)
    
    @property
    def initials(self):
        """Фамилия и инициалы"""
        initials = f"{self.last_name} {self.name[0]}." if self.name else self.last_name
        if self.patronymic:
            initials += f"{self.patronymic[0]}."
        return initials
    
    @property
    def is_alive(self):
        """Проверка, жив ли человек"""
        return self.death_date is None

#TODO: дописать адреса желательно через фиас указав, что это последнее место жительства

