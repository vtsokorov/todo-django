from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название задачи')
    task = models.TextField(blank=False, verbose_name='Формулировка задачи')
    isDone= models.BooleanField(null=True, verbose_name='Состояние задачи', default=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Задача'
        verbose_name_plural = 'Задачи'