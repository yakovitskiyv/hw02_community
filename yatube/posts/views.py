from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import Post, Group, User

# Create your views here.


def index(request):
    post_list = Post.objects.all()
    # Если порядок сортировки определен в классе Meta модели,
    # запрос будет выглядить так:
    # post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, }
    )

# def index(request):
    # latest = Post.objects.all()[:12]
    # return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_of_group = group.group_posts.all()
    paginator = Paginator(posts_of_group, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {"group": group, "page": page}
    return render(request, "group.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts_of_author = author.author_posts.all()
    count_of_posts = author.author_posts.count()
    paginator = Paginator(posts_of_author, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {"author": author, "page": page, "count": count_of_posts}
    return render(request, 'profile.html', context)


def post_view(request, username, post_id):
    author = get_object_or_404(User, username=username)
    post_id = get_object_or_404(Post, id=post_id)
    #post = Post.objects.filter(pk=post_id.id)
    post =Post.objects.get(pk=post_id.id)
    count_of_posts = author.author_posts.count()
    
    context = {"author": author,
               "post": post,
               "count": count_of_posts,
               "post_id": post_id
               }
    return render(request, 'post.html', context)
