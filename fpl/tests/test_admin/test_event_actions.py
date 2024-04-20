from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase, Client

from fpl.admin import EventAdmin
from fpl.models import Event, Fixture, Team, Player, PointsInFixture
from fpl.tests.test_admin.utils import get_admin_change_view_url


class EventAdminViewTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = EventAdmin(Event, self.site)
        self.client = Client()
        user = User.objects.create(username='user', is_staff=True, is_superuser=True)
        self.client.force_login(user)

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.create(name='Gameweek 1', fpl_id=1)
        cls.home_team = Team.objects.create(name='Home Team', fpl_id=1, strength=100, strength_overall_home=100,
                                            strength_overall_away=100, strength_attack_home=100,
                                            strength_attack_away=100,
                                            strength_defence_home=100, strength_defence_away=100)
        cls.away_team = Team.objects.create(name='Away Team', fpl_id=2, strength=100, strength_overall_home=100,
                                            strength_overall_away=100, strength_attack_home=100,
                                            strength_attack_away=100,
                                            strength_defence_home=100, strength_defence_away=100)
        cls.fixture = Fixture.objects.create(fpl_id=1, event=cls.event, team_h=cls.home_team, team_a=cls.away_team)
        cls.player_home = Player.objects.create(first_name='Home', second_name='Player', fpl_id=1, team=cls.home_team,
                                                element_type=1)
        cls.player_away = Player.objects.create(first_name='Away', second_name='Player', fpl_id=2, team=cls.away_team,
                                                element_type=1)

    def test_response(self):
        response = self.client.get(get_admin_change_view_url(self.event))
        self.assertEqual(response.status_code, 200)

    def test_predict_for_all_fixtures_action(self):
        # Check that the players don't have predicted points
        self.assertEqual(PointsInFixture.objects.filter(fixture=self.fixture, player=self.player_home).count(), 0)
        self.admin.predict_for_all_fixtures(request=None, queryset=Event.objects.filter(id=self.event.id))
        # Check that the players have predicted points
        self.assertEqual(PointsInFixture.objects.filter(fixture=self.fixture, player=self.player_home).count(), 1)
