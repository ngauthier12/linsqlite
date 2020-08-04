from tests.test_base import TestBase


class TestSelect(TestBase):

    source_db_path = "cars.sqlite"
    temp_db_path = "temp.sqlite"

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
