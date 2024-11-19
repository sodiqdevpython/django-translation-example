from django.views.generic import ListView
from .models import Course

class ListCours(ListView):
    model = Course
    template_name = 'index.html'