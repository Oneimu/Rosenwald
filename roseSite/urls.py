from django.urls import path
from . import views

# Url congiguration
# always end your routes with a foward slash
urlpatterns = [
    path('', views.index, name='index')
]