from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_testaments, name='index_testaments'),

]