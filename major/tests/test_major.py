from unittest import TestCase


from major.major.major import Major


class TestMajor(TestCase):

    def test_name(self):
        m = Major('foo')
        self.assertEqual('foo', m.get_name())
