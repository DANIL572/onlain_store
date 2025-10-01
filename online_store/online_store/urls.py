"""
URL configuration for online_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""

from django.contrib import admin
from django.urls import path, include
from core.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # Главная страница
    path('users/', include('core.urls')),  # Приложение core
    path('sellers/', include('sellers.urls')),
]




    # path('cart/', include('customers.urls.py')),
    # path('finance/', include('finance.urls.py')),
    # path('products/', include('products.urls.py')),
    # path('reviews/', include('reviews.urls.py')),
    # path('seller/', include('sellers.urls.py')),

    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py.py)
    # подключались к главному приложению с префиксом products/.
    # path('sorting/', include('news.urls.py')),
    # path('', include('news.urls.py')),

