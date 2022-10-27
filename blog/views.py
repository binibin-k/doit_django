from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/index.html', {'posts': posts})

class PostList(ListView):
    model = Post # Post 라는 클래스의 데이터를 가져옴
    # template_name = 'blog/index.html'


# def single_post_page(request, num):
#     post = Post.objects.get(pk=num)
#     return render(request, 'blog/single_post_page.html', {'post':post})

class PostDetail(DetailView):
    model = Post
    # template_name = 'blog/single_post_page.html'