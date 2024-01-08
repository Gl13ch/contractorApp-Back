from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.JobList.as_view(), name='job_list'),
    path('job/<int:pk>', views.JobDetail.as_view(), name='job_detail'),
]