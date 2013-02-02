'''Functional tests using WebTest'''

from django_webtest import WebTest

class TestAUser(WebTest):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_see_homepage(self):
        # Rosie goes to homepage
        root = self.app.get('/')
        # Finish this test
