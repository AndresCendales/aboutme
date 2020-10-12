""" Services views """

# Django
from django.views.generic import ListView 

# Model
from .models import Service, Project

class HomeView(ListView):
    """List Services View"""
    template_name = 'pages/home.html'
    model = Service
    context_object_name = 'portfolio'

    def get_queryset(self):  
        """ Return the services and the projects"""
        return [Service.objects.all(),Project.objects.all()]  
