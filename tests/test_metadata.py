import unittest
import shutil
import os
from linsqlite.Connection import Connection


class TestMetaData(unittest.TestCase):

    source_db_path = "cars.sqlite"
    temp_db_path = "temp.sqlite"

    def setUp(self):
        shutil.copy(self.source_db_path, self.temp_db_path)
        self.connection = Connection(self.temp_db_path)

    def tearDown(self):
        self.connection.close()
        os.remove(self.temp_db_path)

    def test_tables(self):
        expected_table_names = ["cars"]
        tables = self.connection.get_tables()
        table_names = list(map(lambda x: x.name, tables))
        self.assertEqual(expected_table_names, table_names)
