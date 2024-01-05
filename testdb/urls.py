from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.TestingList.as_view(), name='testings_list'), # testing/ will be routed to the TestingList view for handling
    path('testing/<int:pk>', views.TestingDetail.as_view(), name='testing_detail'), # api/contacts will be routed to the ContactDetail view for handling
]