from django.urls import path
from livestreams.views import MainView

urlpatterns = [
    path('start/', MainView.as_view(), name='start'),
]
