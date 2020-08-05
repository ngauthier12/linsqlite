from tests.test_base import TestBase


class TestOrderBy(TestBase):

    def test_order_by(self):
        expected = [
            {'make': 'chevrolet'},
            {'make': 'subaru'},
            {'make': 'toyota'}
        ]
        result = self.connection.cars.order_by(lambda x: x.make).select(lambda x: x.make).execute()
        self.assertEqual(expected, result)

    def test_order_by_descending(self):
        expected = [
            {'make': 'toyota'},
            {'make': 'subaru'},
            {'make': 'chevrolet'}
        ]
        result = self.connection.cars.order_by_descending(lambda x: x.make).select(lambda x: x.make).execute()
        self.assertEqual(expected, result)
