
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contracts/', include('contracts.urls')),
    path('testaments/', include('testaments.urls')),
    path('inheritance_cases/', include('inheritance_cases.urls')),

]
