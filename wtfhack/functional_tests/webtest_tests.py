'''Functional tests using WebTest'''

import time
from django.core.urlresolvers import reverse
from django_webtest import WebTest
from nose.tools import *

from wtfhack.base.models import *
from wtfhack.base.views import *

class TestAUser(WebTest):

    def setUp(self):
        self.python = Language.objects.create(name='python',
                                    learn_url='http://www.diveintopython.net/toc/index.html')
        self.ruby = Language.objects.create(name='ruby',
                                    learn_url="http://tryruby.org/levels/1/challenges/0")

    def tearDown(self):
        pass

    def test_can_see_homepage(self):
        # a ruby repo is created
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language=self.ruby)
        # Goes to homepage
        root = self.app.get('/').follow()  # Follow redirect
        # Sees text
        assert_in('I want to fucking hack', root)

    def test_can_see_language(self):
        # a ruby repo is created
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language=self.ruby)
        # goes to ruby page
        res = self.app.get(reverse(get_repo, args=('ruby',)))
        # sees language
        assert_in('I want to fucking hack', res)
        assert_in('ruby', res)
        
    def test_no_repos(self):
        # goes to ruby page
        res = self.app.get('/')
        assert_in('No projects', res)

        res = res.click('Contribute')

    def test_can_learn(self):
        # a ruby repo is created
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language=self.ruby)

        # goes to ruby page
        res = self.app.get(reverse(get_repo, args=('ruby',)))
        assert_in("I don't fucking know ruby", res)

    def test_can_get_a_new_project(self):
        # a repo is created
        repo1 = Repo.objects.create(full_name='sloria/usv',
                                    language=self.python)
        # another repo is created
        repo2 = Repo.objects.create(full_name='django/django',
                                    language=self.python)
        # goes to page
        res = self.app.get(reverse(get_repo, args=('python',)))

        res = res.click("Fuck that")
        assert_equal(res.status, '200 OK')

    def test_can_submit(self):
        # goes to the homepage
        res = self.app.get('/')
        res = res.click('Submit')


