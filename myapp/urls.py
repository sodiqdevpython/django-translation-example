from django.urls import path
from .views import ListCours

urlpatterns = [
    path('', ListCours.as_view(), name='main')
]