from django.db import models

from django.core.validators import RegexValidator

class Feedback(models.Model):
    feedback_name = models.CharField(max_length=50, verbose_name='Имя покупателя')
    feedback_phone = models.CharField(
        max_length=20,
        verbose_name='Телефон покупателя',
        validators=[RegexValidator(regex=r'^[\+\d\s]+$', message='Телефон должен содержать только цифры')]
    )
    feedback_message = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Обратная связь покупателя'
        verbose_name_plural = 'Обратная связь покупателя'

    def __str__(self):
        return self.feedback_message[:30]
