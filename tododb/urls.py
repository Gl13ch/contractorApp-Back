from django.urls import path
from . import views

urlpatterns = [
    path('punch/', views.PunchList.as_view(), name='punch_list'),
    path('punch/<int:pk>', views.PunchDetail.as_view(), name='punch_detail'),
    path('punchlist/', views.PunchListList.as_view(), name='punchlist_list'),
    path('punchlist/<int:pk>', views.PunchListDetail.as_view(), name='punchlist_detail')
]