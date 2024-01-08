from django.urls import path
from . import views

urlpatterns = [
    path('jobboard/', views.JobBoardList.as_view(), name='jobboard_list'),
    path('jobboard/<int:pk>', views.JobBoardDetail.as_view(), name='jobboard_detail'),
]