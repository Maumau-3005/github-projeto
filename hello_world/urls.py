"""
URL configuration for hello_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hello_world.core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', core_views.home, name='index'),
    path('calendario/', core_views.calendario, name='calendario'),
    path('faq/', core_views.faq, name='faq'),
    path('iniciar_sessao/', auth_views.LoginView.as_view(template_name='registrar.html'), name='iniciar_sessao'),
    path('inscrever_se/', core_views.inscrever_se, name='inscrever_se'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
