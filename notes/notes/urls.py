"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from authapp import views as authapp_views
from homeapp import views as homeapp_views

urlpatterns = [
    path('',authapp_views.signup , name='signup'),
    path('login/',authapp_views.login , name='login'),
    path('home/', homeapp_views.home_create_notes ,name='home_create_notes'),
    path("delete/<int:id>/",homeapp_views.home_delete_note,name='delete_note'),
    path('update/<int:id>/',homeapp_views.home_update_note, name='home_update_note'),
    path('logout/',authapp_views.logout, name='logout'),
    path('add_favourite/<int:id>/',homeapp_views.add_favourites,name='add_favourites'),
    path('remove_favourites/<int:id>/',homeapp_views.remove_favourites,name='remove_favourites'),
    path('recycle_bin/',homeapp_views.recycle_bin, name='recycle_bin'),
    path('restore_note/<int:id>/',homeapp_views.restore_note, name='restore_note'),
    path('permanent_delete/<int:id>/',homeapp_views.permanent_delete, name='permanent_delete'),
    path('delete_account/',authapp_views.delete_account,name='delete_account'),
    path('admin/', admin.site.urls),
]
