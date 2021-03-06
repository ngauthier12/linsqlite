import sqlite3
from linsqlite.Table import Table


class Connection:

    ignored_tables = ["sqlite_sequence"]

    def __init__(self, db_path):
        assert isinstance(db_path, str), "Expecting db_path to be of type str"

        connection = sqlite3.connect(db_path)
        assert connection is not None, "Could not connect to database"
        self.__connection = connection
        self.__cursor = connection.cursor()

        # Fetch meta-data
        tables = []
        for table_name in self.__get_table_names():
            if table_name in self.ignored_tables:
                continue
            column_names = self.__get_column_names(table_name)
            table = Table(self.__cursor, table_name, column_names)
            setattr(self, table_name, table)
            tables.append(table)
        self.__tables = tables

    def close(self):
        self.__connection.close()

    def get_tables(self):
        return self.__tables

    def __get_table_names(self):
        tables_info_query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables_info = self.__cursor.execute(tables_info_query)

        table_names = []
        for row in tables_info.fetchall():
            table_names.append(row[0])
        return table_names

    def __get_column_names(self, table_name):
        table_info_query = "SELECT name FROM PRAGMA_TABLE_INFO('{0}');".format(table_name)
        table_info = self.__cursor.execute(table_info_query)

        column_names = []
        for row in table_info.fetchall():
            column_names.append(row[0])
        return column_names
