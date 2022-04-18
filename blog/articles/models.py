from django.db import models


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    definition = models.CharField('Описание', max_length=140)
    text = models.TextField('Текст')
    date = models.DecimalField(
        'Дата публикации', max_digits=15, decimal_places=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
