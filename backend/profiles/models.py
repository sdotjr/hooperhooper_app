from django.db import models
from django.contrib.auth.models import User

POSITION_CHOICES = [('Guard', 'Guard'), ('Forward', 'Forward'), ('Center', 'Center')]
EXPERIENCE_CHOICES = [('Rookie', 'Rookie'), ('Baller', 'Baller'), ('Hooper', 'Hooper'), ('HooperHooper', 'HooperHooper'), ('MVP', 'MVP')]
GAME_TYPE_CHOICES = [(1, '1v1'), (2, '2v2'), (3, '3v3'), (4, '4v4'), (5, '5v5')]
SKILL_CHOICES = [('Shooter', 'Shooter'), ('Defender', 'Defender'), ('Playmaker', 'Playmaker')]

"""
class HomeCourt(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
"""


class PlayerProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    #home_courts = models.ManyToManyField(HomeCourt)
    height = models.FloatField()  # in centimeters or inches
    weight = models.FloatField()  # in kilograms or pounds
    body_type = models.CharField(max_length=100)  # e.g. Athletic, Bulky, Slim
    position = models.CharField(choices=POSITION_CHOICES, max_length=50)
    experience_level = models.CharField(choices=EXPERIENCE_CHOICES, max_length=50)
    availability = models.JSONField()  # A JSON structure to capture availability
    preferred_game_type = models.PositiveIntegerField(choices=GAME_TYPE_CHOICES)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    vip_status = models.BooleanField(default=False)
    favorite_players = models.TextField(blank=True)
    playstyle_preference = models.CharField(choices=SKILL_CHOICES, max_length=50)
    fitness_status = models.TextField()  # e.g. Fit, Injured, Recovering
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class SkillHighlights(models.Model):
    player_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    skill = models.CharField(choices=SKILL_CHOICES, max_length=50, blank=True)
    custom_skill = models.TextField(blank=True)

class MediaHighlights(models.Model):
    player_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    video_clip = models.FileField(upload_to='media_highlights/', blank=True)
    description = models.TextField(blank=True)

class PlayerRatings(models.Model):
    player_profile = models.ForeignKey(PlayerProfile, related_name='ratings_received', on_delete=models.CASCADE)
    rated_by = models.ForeignKey(PlayerProfile, related_name='ratings_given', on_delete=models.CASCADE)
    skill_rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    sportsmanship_rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

class Endorsements(models.Model):
    endorsed_user = models.ForeignKey(PlayerProfile, related_name='endorsements_received', on_delete=models.CASCADE)
    endorsed_by = models.ForeignKey(PlayerProfile, related_name='endorsements_given', on_delete=models.CASCADE)
    skill_endorsed = models.ForeignKey(SkillHighlights, on_delete=models.CASCADE)

class Accolades(models.Model):
    player_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=200)
    date_awarded = models.DateField()

class SocialFeatures(models.Model):
    player_profile = models.ForeignKey(PlayerProfile, related_name='user_profile', on_delete=models.CASCADE)
    friends = models.ManyToManyField(PlayerProfile, blank=True)
    chat_history = models.JSONField()  # Consider more complex structure or integration with chat services

class RecentMatchHistory(models.Model):
    player_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    date_played = models.DateField()
    score = models.CharField(max_length=100)  # E.g. "21-15"
    teammates = models.ManyToManyField(PlayerProfile, related_name='teammates', blank=True)
    opponents = models.ManyToManyField(PlayerProfile, related_name='opponents', blank=True)

