from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Заголовка"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name = "Дата создание"
    )
    due_date = models.DateTimeField(
        verbose_name = "срок"
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name="Пользователи"
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Такс'
