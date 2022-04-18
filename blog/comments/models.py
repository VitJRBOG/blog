from django.db import models


class Comment(models.Model):
    text = models.TextField('Текст')
    article_id = models.IntegerField('Идентификатор статьи')
    parent_id = models.IntegerField('Идентификатор родительского комментария')
    date = models.DecimalField(
        'Дата публикации', max_digits=15, decimal_places=0)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text
