import types
from linsqlite.Column import Column
from linsqlite.Query import Query


class Table:

    def __init__(self, cursor, table_name, column_names):
        assert isinstance(table_name, str), "Expecting table_name to be of type str"
        assert isinstance(column_names, list), "Expecting column_names to be of type list"

        self.name = table_name
        self.__cursor = cursor

        columns = []
        for column_name in column_names:
            column = Column(column_name)
            setattr(self, column_name, column)
            columns.append(column)
        self.__columns = columns

    def __str__(self):
        column_desc = str(list(map(lambda x: str(x), self.__columns)))
        return "Table '{0}': {1}".format(self.name, column_desc)

    def get_columns(self):
        return self.__columns

    def select(self, predicate):
        query = Query(self.__cursor, self)
        return query.select(predicate)

    def select_all(self):
        return Query(self.__cursor, self)

    def where(self, predicate):
        query = Query(self.__cursor, self)
        return query.where(predicate)

    def order_by(self, predicate):
        query = Query(self.__cursor, self)
        return query.order_by(predicate)

    def order_by_descending(self, predicate):
        query = Query(self.__cursor, self)
        return query.order_by_descending(predicate)

    def take(self, count):
        query = Query(self.__cursor, self)
        return query.take(count)

    def skip(self, count):
        query = Query(self.__cursor, self)
        return query.skip(count)
