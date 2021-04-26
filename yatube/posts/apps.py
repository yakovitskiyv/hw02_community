from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
    verbose_name = 'Управление публикациями posts'


class GroupConfig(AppConfig):
    name = 'group'
    verbose_name = 'Управление сообществами'
