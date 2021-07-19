from django.urls import path
from electronics import views as electronics_views
from django.urls import include, path

urlpatterns = [
    path('recommender',electronics_views.electronics_recommender,name='electronics_recommender'),
]
