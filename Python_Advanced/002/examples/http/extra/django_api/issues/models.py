from django.db import models


class Issue(models.Model):

    name = models.CharField('Назва', max_length=512)
    description = models.TextField('Опис', default='')
    due_date = models.DateField('Виконати до дати')

    class Meta:
        verbose_name = "Нотатка"
        verbose_name_plural = "Нотатки"
