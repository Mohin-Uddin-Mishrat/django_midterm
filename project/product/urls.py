
from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:id>', views.details , name = 'details'),  
    path('buyCar/<int:id>', views.buy , name = 'buy'),  
]

