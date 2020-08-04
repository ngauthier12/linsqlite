import types
from linsqlite.Column import Column
from linsqlite.Query import Query


class Table:

    def __init__(self, cursor, table_name, column_names):
        assert isinstance(table_name, str), "Expecting table_name to be of type str"
        assert isinstance(column_names, list), "Expecting column_names to be of type list"

        self.name = table_name
        self.__cursor = cursor

        for column_name in column_names:
            column = Column(column_name)
            setattr(self, column_name, column)

    def __str__(self):
        column_desc = str(list(map(lambda x: str(x), self.__dict__)))
        return "Table '{0}': {1}".format(self.name, column_desc)

    def select(self, predicate):
        assert isinstance(predicate, types.LambdaType)
        query = Query(self.__cursor, self)
        return query.select(predicate)
