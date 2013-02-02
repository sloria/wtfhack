'''Unit tests for the base app'''

from django.test import TestCase
from nose.tools import assert_equal

from wtfhack.base.models import Repo, Language

class RepoTest(TestCase):

    def setUp(self):
        self.python = Language.objects.create(name='python',
                                    learn_url='http://www.diveintopython.net/toc/index.html')
        self.ruby = Language.objects.create(name='ruby',
                                    learn_url="http://tryruby.org/levels/1/challenges/0")

    def test_model(self):
        assert_equal(len(Repo.objects.all()), 0)
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language=self.ruby)
        assert_equal(len(Repo.objects.all()), 1)
        assert_equal(repo.language.name, 'ruby')

    def test_save_url(self):
        # repo is saved without specifying url
        repo = Repo.objects.create(full_name='ruby/ruby', language=self.ruby)
        # url should default to base url + full name
        assert_equal(repo.url, u'https://github.com/ruby/ruby')

    def test_unicode(self):
        repo = Repo.objects.create(full_name='sloria/usv', language=self.python)
        assert_equal(str(repo), "sloria/usv: python")


class LanguageTest(TestCase):


    def test_model(self):
        lang = Language.objects.create(name='python',
                                    learn_url='http://www.diveintopython.net/toc/index.html')
        assert_equal(len(Language.objects.all()), 1)
        assert_equal(lang.name, 'python')
    def test_all(self):
        python = Language.objects.create(name='python',
                                    learn_url='http://www.diveintopython.net/toc/index.html')
        ruby = Language.objects.create(name='ruby',
                                    learn_url="http://tryruby.org/levels/1/challenges/0")
        assert_equal(Language.all(), [u'python', u'ruby'])


