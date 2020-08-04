import types
from linsqlite.Column import Column
from linsqlite.Condition import Condition


class Query:

    def __init__(self, cursor, table):
        self.__is_executed = False
        self.__cursor = cursor
        self.__table = table
        self.__conditions = []
        self.__columns = []
        self.__results = None

    def select(self, predicate):
        assert isinstance(predicate, types.LambdaType)
        assert not self.__is_executed

        # Only 1 select per query for now.
        assert len(self.__columns) == 0

        # Execute predicate on meta-data, and keep track of selected columns.
        result = predicate(self.__table)
        if isinstance(result, Column):
            self.__columns.append(result)
        elif isinstance(result, tuple):
            assert len(result) > 0
            for column in result:
                assert isinstance(column, Column)
                self.__columns.append(column)

        return self

    def where(self, predicate):
        assert isinstance(predicate, types.LambdaType)
        assert not self.__is_executed

        condition = predicate(self.__table)
        assert isinstance(condition, Condition)
        self.__conditions.append(condition)

        return self

    def __execute(self):
        table_name = self.__table.name

        column_names = "*"
        if len(self.__columns) > 0:
            column_names = ", ".join(list(map(lambda x: x.name, self.__columns)))

        conditions = ""
        if len(self.__conditions) > 0:
            conditions = "WHERE " + " AND ".join(list(map(lambda x: str(x), self.__conditions)))

        query = "SELECT {0} FROM {1} {2};".format(column_names, table_name, conditions)
        #print(query)
        self.__results = self.__cursor.execute(query)

    def __iter__(self):
        if not self.__is_executed:
            self.__execute()
        return self.__results.__iter__()

    def __next__(self):
        return self.__results.__next__()

    def __str__(self):
        result_strings = list(map(lambda x: str(x), self))
        return "[{0}]".format(", ".join(result_strings))
