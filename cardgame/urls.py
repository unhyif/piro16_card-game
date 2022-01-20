from django.urls import path
from .views import *

app_name = "cardgame"

urlpatterns = [
    path('attack/', attack, name="attack"),
    path('detail/<int:pk>', detail, name="detail"),
]