from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    # ex: /search/
    path('', views.PublicPostIndexView.as_view(), name='top'),
]