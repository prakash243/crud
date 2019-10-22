"""cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from cruds_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.createform, name='createform'),
    path('', views.formdata, name='formdata'),
    path('update/<int:student_id>', views.updateform, name='updateform'),
    path('delete/<int:student_id>', views.delete, name='delete'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit, name='submit'),
    path('subscribe/', views.subscribe, name = 'subscribe'),

]
