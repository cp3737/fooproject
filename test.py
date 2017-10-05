from django.test import TestCase

class FooAPITestCase(TestCase):

    def setUp(self):
        pass

    def test_pass(self):
        assert True is True

#    def test_fail(self):
#        assert False is True

    def tearDown(self):
        pass
