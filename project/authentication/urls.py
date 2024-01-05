
from django.urls import path , include
from . import views
urlpatterns = [
    path('register/', views.register , name = 'register'),
    path('login/', views.userLoginView.as_view() , name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    path('userChange/', views.changeuser, name = 'changeuser'),
]
