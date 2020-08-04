from tests.test_base import TestBase


class TestMetaData(TestBase):

    def test_tables(self):
        expected_table_names = ['cars']
        tables = self.connection.get_tables()
        table_names = list(map(lambda x: x.name, tables))
        self.assertEqual(expected_table_names, table_names)

    def test_columns(self):
        expected_column_names = ['make', 'model', 'is_electric', 'year', 'id']
        columns = self.connection.cars.get_columns()
        column_names = list(map(lambda x: x.name, columns))
        self.assertEqual(expected_column_names, column_names)
