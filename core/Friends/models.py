from django.db import models
from Accounts.models import UserProfile


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='received_requests')
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def accept(self):
        if not self.is_accepted and not self.is_rejected:
            self.is_accepted = True
            self.save()

    def reject(self):
        if not self.is_accepted and not self.is_rejected:
            self.is_rejected = True
            self.save()


class Friend(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='friend_of')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')

    def unfriend(self):
        self.delete()
