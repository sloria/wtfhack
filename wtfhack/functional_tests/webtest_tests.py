'''Functional tests using WebTest'''

from django.core.urlresolvers import reverse
from django_webtest import WebTest
from nose.tools import *

from wtfhack.base.models import Repo
from wtfhack.base.views import *

class TestAUser(WebTest):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_see_homepage(self):
        # a ruby repo is created
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language='ruby')
        # Goes to homepage
        root = self.app.get('/').follow()  # Follow redirect
        # Sees text
        assert_in('I want to fucking hack', root)

    def test_homepage_with_repo(self):
        # a ruby repo is created
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language='ruby',
                                    description='The Ruby Programming Language')
        # goes to homepage
        res = self.app.get('/').follow()  # Follow redirect
        # The repo name and description are shown
        assert_in('ruby/ruby', res)
        assert_in('The Ruby Programming Language', res)


    def test_can_see_language(self):
        # a ruby repo is created
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language='ruby')
        # goes to ruby page
        res = self.app.get(reverse(get_repo, args=('ruby',)))
        # sees language
        assert_in('I want to fucking hack', res)
        assert_in('ruby', res)
        
    def test_no_repos(self):
        # goes to ruby page
        res = self.app.get(reverse(get_repo, args=('ruby',)))
        assert_in('Fuck. No projects in this language.', res)

