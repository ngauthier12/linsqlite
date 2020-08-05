from tests.test_base import TestBase


class TestLimitOffset(TestBase):

    def test_take(self):
        expected = [
            {'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018},
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
        ]
        result = self.connection.cars.take(2).execute()
        self.assertEqual(expected, result)

    def test_take_and_skip(self):
        expected = [
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017},
        ]
        result = self.connection.cars.take(2).skip(1).execute()
        self.assertEqual(expected, result)

    def test_skip_no_take(self):
        def do_query():
            self.connection.cars.skip(1).execute()
        self.assertRaises(AssertionError, do_query)
