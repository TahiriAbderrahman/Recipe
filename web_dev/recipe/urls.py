from django.urls import path
from .views import list_recette, create_recette
urlpatterns=[
    path('recette/', list_recette, name='recette'),
    path('create/', create_recette, name='create_recette'),
]