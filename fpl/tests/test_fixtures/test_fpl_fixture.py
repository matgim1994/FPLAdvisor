from django.test import TestCase
from fpl.models import Team, Fixture


class FPLFixtureTestCase(TestCase):
    fixtures = ["fpl"]

    def test_fpl_fixture_loaded(self):
        self.assertGreater(Team.objects.count(), 0)
        self.assertGreater(Fixture.objects.count(), 0)
