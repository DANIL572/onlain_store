from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Users, Categories
from .templatetags.forms import UsersForm  # Исправил импорт формы

class UserList(ListView):
    model = Users
    ordering = 'name'
    template_name = 'users.html'
    context_object_name = 'users'

class CategoriesDetail(DetailView):
    model = Categories
    template_name = 'categories.html'
    context_object_name = 'categories'

class UsersCreate(CreateView):
    form_class = UsersForm
    model = Users
    template_name = 'create_core.html'
    success_url = '/'  # Добавьте URL для перенаправления после успешного создания