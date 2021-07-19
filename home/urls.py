from django.urls import path
from home import views as home_views
from django.urls import include, path

urlpatterns = [
    path('',home_views.home,name='home'),
]
