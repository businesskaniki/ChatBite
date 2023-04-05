from django.test import TestCase
from Accounts.models import UserProfile

class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, UserProfile)
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))
        self.assertFalse(self.user.is_admin)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'testuser')
