from django.shortcuts import render, get_object_or_404

from .models import Post, Group

# Create your views here.


def index(request):
    latest = Post.objects.all()[:12]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_of_group = group.group_posts.all()[:12]
    context = {"group": group, "posts": posts_of_group}
    return render(request, "group.html", context)
