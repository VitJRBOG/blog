from django.db import models


class Comment(models.Model):
    text = models.TextField('Текст')
    article_id = models.IntegerField('Идентификатор статьи')
    parent_id = models.IntegerField('Идентификатор родительского комментария')
    date = models.IntegerField('Дата публикации')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text
