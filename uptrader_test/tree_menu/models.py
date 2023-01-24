from django.db import models


class Menu(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='MenuCategories',
        on_delete=models.CASCADE,
        related_name='menu'
    )
    link = models.CharField(
        verbose_name='Ссылка на раздел меню',
        max_length=250,
        blank=True,
    )
    parent = models.ForeignKey(
        verbose_name='Родительский раздел',
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuCategories(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        unique=True
    )
    systemic_name = models.CharField(
        verbose_name='Системное название',
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = 'Категория Меню'
        verbose_name_plural = 'Категории Меню'
        ordering = ['name']

    def __str__(self):
        return self.name
