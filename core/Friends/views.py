from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Friend, FriendRequest
from .serializers import FriendRequestSerializer, FriendSerializer


class FriendListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = Friend.objects.filter(user=user)
        return friends


class FriendRequestListView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friend_requests = FriendRequest.objects.filter(receiver=user)
        return friend_requests


class FriendRequestCreateView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendRequestAcceptView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.accept()
        return Response(self.get_serializer(friend_request).data)


class FriendRequestRejectView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.reject()
        return Response(self.get_serializer(friend_request).data)


class FriendDeleteView(generics.DestroyAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        friend = self.get_object()
        if friend.user == request.user or friend.friend == request.user:
            friend.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
