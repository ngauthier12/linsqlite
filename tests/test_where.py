from tests.test_base import TestBase


class TestWhere(TestBase):

    def test_greater_than(self):
        expected = [{'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018}]
        result = self.connection.cars.where(lambda x: x.year > 2017).execute()
        self.assertEqual(expected, result)

    def test_less_than(self):
        expected = [{'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013}]
        result = self.connection.cars.where(lambda x: x.year < 2017).execute()
        self.assertEqual(expected, result)

    def test_equal(self):
        expected = [{'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018}]
        result = self.connection.cars.where(lambda x: x.year == 2018).execute()
        self.assertEqual(expected, result)

    def test_not_equal(self):
        expected = [
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017}
        ]
        result = self.connection.cars.where(lambda x: x.year != 2018).execute()
        self.assertEqual(expected, result)
