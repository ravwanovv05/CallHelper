from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статусы смены'
        ordering = ('sort',)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Replacement(models.Model):
    group = models.ForeignKey(
        'breaks.Group', models.CASCADE, 'replacements',
        verbose_name='Группа'
    )
    date = models.DateField('Дата смены')
    break_start = models.TimeField('Начало обеда', null=True, blank=True)
    break_end = models.TimeField('Конец обеда', null=True, blank=True)
    break_max_duration = models.PositiveSmallIntegerField(
        'Максимальная длительность обеда', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self):
        return f"Смена №{self.pk} для {self.group}"


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        User, models.CASCADE,
        verbose_name='Сотрудник'
    )
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE,
        verbose_name='Смена'
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', models.RESTRICT, 'replacement_employees',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Смена - Сотрудник'
        verbose_name_plural = 'Смены - Сотрудники'

    def __str__(self):
        return f"Смена {self.replacement} для {self.employee}"
