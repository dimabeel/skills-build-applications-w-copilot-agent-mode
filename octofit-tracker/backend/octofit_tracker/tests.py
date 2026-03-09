from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class BasicModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', activity_type='Run', duration=30, team='Test Team')
        self.assertEqual(str(activity), 'testuser - Run')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=50)
        self.assertEqual(str(leaderboard), 'Test Team: 50')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups')
        self.assertEqual(str(workout), 'Pushups')
