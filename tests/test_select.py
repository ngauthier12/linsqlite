from tests.test_base import TestBase


class TestSelect(TestBase):

    def test_select_single(self):
        expected = [
            {'make': 'chevrolet'},
            {'make': 'toyota'},
            {'make': 'subaru'}
        ]
        result = self.connection.cars.select(lambda x: x.make).execute()
        self.assertEqual(expected, result)

    def test_select_tuple(self):
        expected = [
            {'model': 'bolt', 'year': 2018},
            {'model': '86', 'year': 2013},
            {'model': 'forester', 'year': 2017}
        ]
        result = self.connection.cars.select(lambda x: (x.model, x.year)).execute()
        self.assertEqual(expected, result)

    def test_select_all(self):
        expected = [
            {'id': 1, 'is_electric': 1, 'make': 'chevrolet', 'model': 'bolt', 'year': 2018},
            {'id': 2, 'is_electric': 0, 'make': 'toyota', 'model': '86', 'year': 2013},
            {'id': 3, 'is_electric': 0, 'make': 'subaru', 'model': 'forester', 'year': 2017}
        ]
        result = self.connection.cars.select_all().execute()
        self.assertEqual(expected, result)

    def test_select_after_execute(self):
        query = self.connection.cars.where(lambda x: x.year > 2000)
        query.execute()

        def do_select():
            query.select(lambda x: x.make)
        self.assertRaises(AssertionError, do_select)

    def test_wrong_arg_type(self):
        def do_query():
            self.connection.cars.select(0)
        self.assertRaises(AssertionError, do_query)

    def test_wrong_lambda_return_type(self):
        def do_query():
            self.connection.cars.select(lambda x: 0)
        self.assertRaises(AssertionError, do_query)

    def test_wrong_lambda_tuple(self):
        def do_query():
            self.connection.cars.select(lambda x: (x.make, 0))
        self.assertRaises(AssertionError, do_query)

    def test_double_select(self):
        def do_query():
            self.connection.cars.select(lambda x: x.make).select(lambda x: x.model)
        self.assertRaises(AssertionError, do_query)

    def test_none_arg(self):
        def do_query():
            self.connection.cars.select(None)
        self.assertRaises(AssertionError, do_query)

    def test_chaining(self):
        query = self.connection.cars.where(lambda x: x.year > 2000)
        query2 = query.select(lambda x: x.make)
        self.assertEqual(query, query2)


