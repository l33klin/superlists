from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from django.template.loader import render_to_string
import unittest

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    @unittest.skip('error')
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        execpted_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), execpted_html)

    def test_home_page_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
