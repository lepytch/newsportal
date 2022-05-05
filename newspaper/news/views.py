from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView


class Posts(ListView):
    model = Post
    template_name = 'news/base.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'