import sqlite3


class Connection:

    def __init__(self, db_path):
        assert isinstance(db_path, str), "Expecting db_path to be of type str"

        connection = sqlite3.connect(db_path)
        assert connection is not None, "Could not connect to database"
        self.connection = connection
