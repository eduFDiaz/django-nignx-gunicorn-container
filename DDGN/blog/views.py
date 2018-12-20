from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category

from .forms import PostForm


def post_list(request):
    # Returns a list of Posts ordered by date, newest first
    categories = Category.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': posts, 'categories': categories}
    template = 'blog/post_list.html'
    return render(request, template, context)


def post_detail(request, pk, slug):
    # Returns a single post
    post = get_object_or_404(Post, pk=pk, slug=slug)
    categories = Category.objects.all()
    template = 'blog/post_detail.html'
    context = {'post': post, 'categories': categories}
    return render(request, template, context)


def post_new(request):
    # Returns a view to create a post
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk, slug):
    # Returns a view to edit the post
    post = get_object_or_404(Post, pk=pk, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_list_by_category(request, category_slug):
    # List of posts filtered by category
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category).order_by('-published_date')
    template = 'blog/post_by_category.html'
    context = {'posts': posts, 'category': category, 'categories': categories}
    return render(request, template, context)
