from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.TestingList.as_view(), name='testings_list'), # testing/ will be routed to the TestingList view for handling
]