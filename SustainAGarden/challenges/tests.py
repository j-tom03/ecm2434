from django.test import TestCase
from challenges.models import Challenge, User

class ChallengeTestCase(TestCase):
    def test_challenge_creation(self):
        challenge = Challenge.objects.create(name="Test Challenge", description="This is a test challenge", points=100)
        self.assertEqual(challenge.name, "Test Challenge")
        self.assertEqual(challenge.description, "This is a test challenge")
        self.assertEqual(challenge.points, 100)

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", password="testpassword", email="test@test.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@test.com")
