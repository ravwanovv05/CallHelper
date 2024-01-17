from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'breaks',
        verbose_name='Смена'
    )
    employee = models.ForeignKey(
        User, models.CASCADE, 'breaks', verbose_name='Сотрудник'
    )
    break_start = models.TimeField('Начало обеда', null=True, blank=True)
    break_end = models.TimeField('Конец обеда', null=True, blank=True)
    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT, 'breaks', verbose_name='Статус',
        blank=True
    )

    class Meta:
        verbose_name = 'Обед'
        verbose_name_plural = 'Обеды'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f"{self.employee} ({self.pk})"
