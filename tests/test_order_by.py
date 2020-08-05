from tests.test_base import TestBase


class TestOrderBy(TestBase):

    def test_order_by(self):
        expected = [
            {'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017},
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
        ]
        result = self.connection.cars.order_by(lambda x: x.make).execute()
        self.assertEqual(expected, result)

    def test_order_by_descending(self):
        expected = [
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017},
            {'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018},
        ]
        result = self.connection.cars.order_by_descending(lambda x: x.make).execute()
        self.assertEqual(expected, result)
