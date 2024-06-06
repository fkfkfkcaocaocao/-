from . views import user
from django.urls import path
from . import views


app_name = 'userApp'

urlpatterns = [

    path('user/', views.user, name=user),
]