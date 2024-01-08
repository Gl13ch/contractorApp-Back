from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('address/', views.AddressList.as_view(), name='address_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('address/<int:pk>',views.AddressDetail.as_view(), name='address_detail'),
    path('users/login', csrf_exempt(views.check_login), name="check_login"),
]