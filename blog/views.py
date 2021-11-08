from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def posts(request):
    """ A view for the blog page """
    
    posts = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(posts, 4)  # Maximum 4 posts on each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'blog_page': 'active',
        'page': page,
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    """ A view for each blog post """

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)