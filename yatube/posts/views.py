from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from .forms import PostForm
from django.shortcuts import redirect


def index(request):
    selected_posts = Post.objects.all()[:10]
    return render(request, "index.html", {"posts": selected_posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form.save()

            return redirect('index')

        return render(request, 'new.html', {'form': form})

    form = PostForm()
    return render(request, 'new.html', {'form': form})

