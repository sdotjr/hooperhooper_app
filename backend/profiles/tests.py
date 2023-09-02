from django.test import TestCase
from django.contrib.auth.models import User
from .models import PlayerProfile

class PlayerProfileModelTest(TestCase):

    def setUp(self):
      
        self.player = User.objects.create_player(
            username='sdotjr',
            password='password'
        )

        self.player_profile = PlayerProfile.objects.create(
            user=self.user,
            age=32,
            height=210.0,
            weight=69.0,
            body_type="Average",
            position="Guard",
            experience_level="Baller",
            preferred_game_type=5,
            playstyle_preference="Shooter",
            fitness_status="Fit"
        )
        self.user_profile.home_courts.add(self.court)

    def test_user_profile_creation(self):
        self.assertEqual(self.player_profile.age, 25)
        self.assertEqual(self.player_profile.position, "Guard")
        self.assertEqual(self.player_profile.experience_level, "Baller")
        self.assertEqual(self.player_profile.preferred_game_type, 1)
        self.assertIn(self.court, self.player_profile.home_courts.all())