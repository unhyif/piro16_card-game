from django.urls import path
from . import views

app_name = 'cardgame'

urlpatterns = [
    path('', views.main_ready, name = 'main_ready'),
    path('main/', views.main, name = 'main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('attack/', views.attack, name='attack'),
    #path('defend/<int:pk>', views.defend, name='defend'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    #path('list/', views.list, name='list'),
   path('delete/<int:pk>/', views.delete, name='delete'),
    #path('ranking/', views.ranking, name='ranking'),
]


