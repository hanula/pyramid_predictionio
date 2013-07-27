
import unittest
from nose.tools import assert_equal


class TestBar(unittest.TestCase):

    def call_FUT(self, count):
        from pypkg_template.foo import bar
        return bar(count)

    def test_friday_sunday(self):
        for day in (5, 6):
            assert_equal(self.call_FUT(day), "I'm in a bar")

    def test_workday(self):
        for day in list(range(1, 5)) + [7]:
            assert_equal(self.call_FUT(day), "No bar tonight")
