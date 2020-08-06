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

    def test_multiple_order_by(self):
        expected = [
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017},
            {'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018},
        ]
        result = self.connection.cars.order_by_descending(lambda x: x.make).order_by(lambda x: x.year).execute()
        self.assertEqual(expected, result)

    def test_multiple_order_by_same(self):
        expected = [
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017},
            {'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018},
        ]
        result = self.connection.cars.order_by_descending(lambda x: x.make).order_by(lambda x: x.make).execute()
        self.assertEqual(expected, result)

    def test_arg_none(self):
        def do_query():
            self.connection.cars.order_by(None)
        self.assertRaises(AssertionError, do_query)

    def test_arg_wrong_type(self):
        def do_query():
            self.connection.cars.order_by(0)
        self.assertRaises(AssertionError, do_query)

    def test_arg_wrong_lambda_return(self):
        def do_query():
            self.connection.cars.order_by(lambda x: 0)
        self.assertRaises(AssertionError, do_query)

    def test_order_by_after_execute(self):
        query = self.connection.cars.select_all()
        query.execute()

        def do_order_by():
            query.order_by(lambda x: x.year)

        self.assertRaises(AssertionError, do_order_by)

    def test_chaining(self):
        query = self.connection.cars.select_all()
        query2 = query.order_by(lambda x: x.make)
        self.assertEqual(query, query2)
