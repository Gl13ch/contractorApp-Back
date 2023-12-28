from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('testing/', views.TestingList.as_view(), name='testings_list'), # api/contacts will be routed to the TestingList view for handling
]