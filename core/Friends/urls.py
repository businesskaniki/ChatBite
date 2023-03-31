from django.urls import path
from .views import (FriendListView, FriendRequestListView,
                    FriendRequestCreateView, FriendRequestAcceptView,
                    FriendRequestRejectView, FriendDeleteView)

app_name = 'friends'

urlpatterns = [
    path('', FriendListView.as_view(), name='friend_list'),
    path('requests/', FriendRequestListView.as_view(), name='friend_requests'),
    path('send/', FriendRequestCreateView.as_view(),
         name='send_friend_request'),
    path('request/accept/<int:pk>/', FriendRequestAcceptView.as_view(),
         name='accept_friend_request'),
    path('request/reject/<int:pk>/', FriendRequestRejectView.as_view(),
         name='reject_friend_request'),
    path('delete/<int:pk>/', FriendDeleteView.as_view(), name='delete_friend'),
]
