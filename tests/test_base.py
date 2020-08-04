import unittest
import shutil
import os
from linsqlite.Connection import Connection


class TestBase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.source_db_path = "cars.sqlite"
        self.temp_db_path = "temp.sqlite"

        if not os.path.exists(self.source_db_path):
            self.source_db_path = "tests/" + self.source_db_path
            self.temp_db_path = "tests/" + self.temp_db_path

    def setUp(self):
        shutil.copy(self.source_db_path, self.temp_db_path)
        self.connection = Connection(self.temp_db_path)

    def tearDown(self):
        self.connection.close()
        os.remove(self.temp_db_path)