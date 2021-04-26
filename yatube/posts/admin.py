from .models import Post, Group
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "pub_date", "author")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "title", "slug", "description")
    search_fields = ("slug",)
    list_filter = ("slug",)
    empty_value_display = "-пусто-"


# при регистрации модели Post источником конфигураци
# для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
