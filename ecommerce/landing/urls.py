from django.urls import path
from landing import views
urlpatterns = [
    path('', views.landing, name='landing'),
    path('sendMessage/', views.sendMessage, name='sendMessage'),
]