from django.test import TestCase
from fpl.models import Team


class FPLFixtureTestCase(TestCase):
    fixtures = ["fpl"]

    def test_fpl_fixture_loaded(self):
        self.assertGreater(Team.objects.count(), 0)
