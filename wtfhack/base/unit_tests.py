'''Unit tests for the base app'''

from django.test import TestCase

class ExampleTest(TestCase):
    '''An example unit test case.'''
    def test_add(self):
        self.assertEqual(1+1, 2)