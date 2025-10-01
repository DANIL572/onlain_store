from django.urls import path
# Импортируем созданное нами представление
from .views import UserList, UsersCreate, CategoriesDetail


urlpatterns = [
   path('', UserList.as_view(), name='users_list'),
   path('create/', UsersCreate.as_view(), name='users_create'),
   path('<int:pk>/', CategoriesDetail.as_view(), name='categories_detail'),

]