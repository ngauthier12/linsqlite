import sqlite3
from linsqlite.Table import Table


class Connection:

    def __init__(self, db_path):
        assert isinstance(db_path, str), "Expecting db_path to be of type str"

        connection = sqlite3.connect(db_path)
        assert connection is not None, "Could not connect to database"
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__table_by_name = {}

    def get_table(self, table_name):
        assert isinstance(table_name, str), "Expecting db_path to be of type str"

        # If table meta-data is already available, return it
        if table_name in self.__table_by_name:
            return self.__table_by_name[table_name]

        # Otherwise, get column_names and create table meta-data
        column_names = self.__get_column_names(table_name)
        table = Table(table_name, column_names)
        self.__table_by_name[table_name] = table
        return table

    def __get_column_names(self, table_name):
        table_info_query = "SELECT name FROM PRAGMA_TABLE_INFO('{0}');".format(table_name)
        table_info = self.__cursor.execute(table_info_query)

        column_names = []
        for row in table_info.fetchall():
            column_names.append(row[0])

        return column_names
