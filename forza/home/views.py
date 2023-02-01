from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView


from .forms import RegisterUserForm, LoginUserForm, ContactForm


def Home(request):
    return render(request, 'home/home.html')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class LoggoutUser(LogoutView):
    form_class = logout
    template_name = 'home/login.html'

class Contact(FormView):
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обратная связь'
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

