"""mood_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('art', views.art,name='art'),
    path('cooking', views.cooking,name='cooking'),
    path('exercise', views.exercise,name='exercise'),
    path('gaming', views.gaming,name='gaming'),
    path('meme', views.meme,name='meme'),
    path('page2', views.page2,name='page2'),
    path('page3', views.page3,name='page3'),
    path('woof', views.woof,name='woof'),
    path('meow', views.meow,name='meow'),

]
