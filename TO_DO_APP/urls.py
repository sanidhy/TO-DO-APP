"""TO_DO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from TO_DO_APP import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path('login/',views.login,name="login"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('second_page/',views.second_page,name="second_page"),
    path('add-todo/',views.add_todo,name="add-todo"),
    path('delete-todo/<int:id>' , views.delete_todo,name="delete_todo" ), 
    path('change-status/<int:id>/<str:status>' , views.change_todo,name="change_todo" ), 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
