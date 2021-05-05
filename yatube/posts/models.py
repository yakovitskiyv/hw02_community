from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='Название сообщества'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Адрес'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание сообщества'
    )

    class Meta:
        verbose_name = ('Сообщество')
        verbose_name_plural = ('Сообщества')
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):

    text = models.TextField(
        verbose_name='Текст публикации'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        related_name='author_posts',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        related_name='group_posts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Сообщество'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']
