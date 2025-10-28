from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import Post
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Post
    template_name = 'app/blog_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'app/blog_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')