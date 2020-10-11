from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
"""
    Class MainView - main page
"""

class MainView(TemplateView):
  template_name = 'index.html'

