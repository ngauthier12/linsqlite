import types
from linsqlite.Column import Column

class Query:

    def __init__(self, table):
        self.__is_executed = False
        self.__table = table
        self.__filters = []
        self.__columns = []

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

    def __execute(self):
        # todo
        pass

    def __iter__(self):
        if not self.__is_executed:
            self.__execute()
        return self.__results.__iter__()

    def __next__(self):
        return self.__results.__next__()
