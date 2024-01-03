from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
]