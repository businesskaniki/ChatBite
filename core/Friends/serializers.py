from rest_framework import serializers
from Accounts.models import UserProfile
from .models import Friend, FriendRequest


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ("id", "user", "friend", "created_at")


class FriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "sender",
            "receiver",
            "is_accepted",
            "is_rejected",
            "created_at",
        )

    def get_sender(self, obj):
        return obj.sender.username

    def get_receiver(self, obj):
        return obj.receiver.username


class FriendRequestCreateSerializer(serializers.ModelSerializer):
    receiver = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = FriendRequest
        fields = ("id", "sender", "receiver", "created_at")

    def create(self, validated_data):
        sender = self.context["request"].user
        # get the ID of the receiver
        receiver_id = validated_data["receiver"].id
        friend_request = FriendRequest.objects.create(
            sender=sender, receiver_id=receiver_id
        )
        return friend_request


class FriendRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ("id", "is_accepted", "is_rejected", "created_at")

    def update(self, instance, validated_data):
        if validated_data.get("is_accepted", False):
            instance.accept()
        elif validated_data.get("is_rejected", False):
            instance.reject()
        return instance
