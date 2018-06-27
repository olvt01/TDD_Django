from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page


class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    #
    #
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('UTF8')
    #     expected_html = render_to_string('lists/home.html')
    #     self.assertEqual(html, expected_html)

    # These two long-winded tests into one: test_uses_home_templates

    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')


    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())


    # def test_home_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #     self.assertIn('A new list item', response.content.decode())
    #

