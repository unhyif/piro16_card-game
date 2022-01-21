from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_ready, name = 'main_ready'),
    path('main/', views.main, name = 'main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('attack/', views.attack, name="attack"),
    path('detail/<int:pk>', views.detail, name="detail"),
]
