from django.urls import path
from api import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostInfo),
    path('login/', views.login),
    path('logout/', views.logout),
]
