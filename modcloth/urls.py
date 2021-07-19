from django.urls import path
from modcloth import views as modcloth_views
from django.urls import include, path

urlpatterns = [
    path('recommender',modcloth_views.modcloth_recommender,name='modcloth_recommender'),
]
