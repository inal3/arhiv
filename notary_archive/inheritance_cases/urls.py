from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_ic, name='index_ic'),
    path('1/', views.detail_ic, name='detail_ic')

]