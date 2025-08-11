from django.urls import path
from .views import UserAPI
from . import views 

urlpatterns=[
    path('users/',UserAPI.as_view(),name='user api')
]