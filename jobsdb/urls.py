from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.JobList.as_view(), name='job_list'),
    path('address/', views.AddressList.as_view(), name='address_list'),
    path('job/<int:pk>', views.JobDetail.as_view(), name='job_detail'),
    path('address/<int:pk>',views.AddressDetail.as_view(), name='address_detail'),
]