'''Unit tests for the base app'''

from django.test import TestCase
from nose.tools import assert_equal

from wtfhack.base.models import Repo

class RepoTest(TestCase):
    def test_model(self):
        assert_equal(len(Repo.objects.all()), 0)
        repo = Repo.objects.create(full_name='ruby/ruby',
                                    language='ruby')
        assert_equal(len(Repo.objects.all()), 1)
        assert_equal(repo.language, 'ruby')

    def test_save_url(self):
        # repo is saved without specifying url
        repo = Repo.objects.create(full_name='ruby/ruby', language='ruby')
        # url should default to base url + full name
        assert_equal(repo.url, u'https://github.com/ruby/ruby')

    def test_unicode(self):
        repo = Repo.objects.create(full_name='sloria/usv', language='python')
        assert_equal(str(repo), "sloria/usv: python")

    def test_all_languages(self):
        repo1 = Repo.objects.create(full_name='sloria/usv',
                                    language='python')
        repo2 = Repo.objects.create(full_name='ruby/ruby',
                                    language='ruby')
        assert_equal(Repo.all_languages(), [u'python', u'ruby'])

