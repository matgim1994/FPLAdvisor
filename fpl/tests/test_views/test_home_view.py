from django.test import TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):

    def test_get_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'hello world')
