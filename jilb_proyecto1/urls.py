"""jilb_proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from App1 import views as App1
from App2 import views as App2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola1/', App1.display),
    path('ahora/', App1.displayDateTime),
    path('lista/', App1.display2),
    path('hola2/', App2.display1),
    path('texto/', App2.display2),
]
