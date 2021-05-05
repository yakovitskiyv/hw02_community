from django import template
# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр
register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


# синтаксис @register... , под которой описана функция addclass() -
# это применение "декораторов", функций, обрабатывающих функции
# мы скоро про них расскажем. Не бойтесь соб@к
# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр


@register.filter
def uglify(uglify):
    count = 0
    letters_string = ''

    for letters in uglify:
        count += 1
        if count % 2 == 0:
            letters_string += letters.upper()

        else:
            letters_string += letters.lower()
    return letters_string
