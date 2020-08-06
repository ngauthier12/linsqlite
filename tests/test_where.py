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

    def test_none_arg(self):
        def do_query():
            self.connection.cars.where(None)
        self.assertRaises(AssertionError, do_query)

    def test_wrong_arg_typ(self):
        def do_query():
            self.connection.cars.where(0)
        self.assertRaises(AssertionError, do_query)

    def test_wrong_lambda_return_type(self):
        def do_query():
            self.connection.cars.where(lambda x: 0)
        self.assertRaises(AssertionError, do_query)

    def test_multiple_where(self):
        expected = [{'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018}]
        result = self.connection.cars.where(lambda x: x.year > 2017).where(lambda x: x.id == 1).execute()
        self.assertEqual(expected, result)

    def test_where_string(self):
        expected = [{'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018}]
        result = self.connection.cars.where(lambda x: x.model == 'bolt').execute()
        self.assertEqual(expected, result)

    def test_where_after_execute(self):
        query = self.connection.cars.select(lambda x: x.make)
        query.execute()

        def do_where():
            query.where(lambda x: x.year > 2000)
        self.assertRaises(AssertionError, do_where)

    def test_chaining(self):
        query = self.connection.cars.where(lambda x: x.year > 2017)
        query2 = query.where(lambda x: x.id == 1)
        self.assertEqual(query, query2)
