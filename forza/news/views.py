from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *

menu = [
    {'name':'Добавить статью', 'url_name':'add_post'}
]

class post_list(ListView):
    paginate_by = 3
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        new_menu = menu.copy()
        if not self.request.user.is_authenticated:
            new_menu.pop(0)
        context['menu'] = new_menu
        return context

class post_category(ListView):
    paginate_by = 3
    model = Post
    # context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        new_menu = menu.copy()
        if not self.request.user.is_authenticated:
            new_menu.pop(0)
        context['menu'] = new_menu
        return context

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], publish=True).select_related('cat')

class post_show(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

class post_add(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'news/post_create.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True          #доступ запрещен



