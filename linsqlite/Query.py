import types
from linsqlite.Column import Column
from linsqlite.Condition import Condition
from linsqlite.OrderInstruction import *


class Query:

    def __init__(self, cursor, table):
        self.__is_executed = False
        self.__cursor = cursor
        self.__table = table
        self.__conditions = []
        self.__columns = []
        self.__order_instructions = []
        self.__skip = None
        self.__take = None
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

    def order_by(self, predicate):
        self.__order_by(predicate, OrderDirection.ASCENDING)
        return self

    def order_by_descending(self, predicate):
        self.__order_by(predicate, OrderDirection.DESCENDING)
        return self

    def __order_by(self, predicate, direction):
        assert isinstance(predicate, types.LambdaType)
        assert not self.__is_executed

        column = predicate(self.__table)
        assert isinstance(column, Column)

        order_instruction = OrderInstruction(column, direction)
        self.__order_instructions.append(order_instruction)

    def take(self, count):
        assert isinstance(count, int) and count > 0, "take expects positive integer 'count'"
        assert self.__take is None, "only 1 take can be specified by query"
        self.__take = count
        return self

    def skip(self, count):
        assert isinstance(count, int) and count > 0, "skip expects positive integer 'count'"
        assert self.__skip is None, "only 1 skip can be specified by query"
        assert self.__take is not None, "skip statement can only be used after a take statement"
        self.__skip = count
        return self

    def execute(self):
        if not self.__is_executed:
            self.__execute()
        return self.__results

    def __execute(self):
        # {0} column_names
        column_names = "*"
        if len(self.__columns) > 0:
            column_names = ", ".join(list(map(lambda x: x.name, self.__columns)))

        # {1} column_names
        table_name = self.__table.name

        # {2} conditions
        conditions = ""
        if len(self.__conditions) > 0:
            conditions = "WHERE " + " AND ".join(list(map(lambda x: str(x), self.__conditions)))

        # {3} order_instructions
        order_instructions = ""
        if len(self.__order_instructions) > 0:
            order_instructions = "ORDER BY " + ", ".join(list(map(lambda x: str(x), self.__order_instructions)))

        # {4} limit
        limit = ""
        if self.__take is not None:
            limit = "LIMIT {0}".format(str(self.__take))

        # {5} offset
        offset = ""
        if self.__skip is not None:
            offset = "OFFSET {0}".format(str(self.__skip))

        query = "SELECT {0} FROM {1} {2} {3} {4} {5};".format(
            column_names,
            table_name,
            conditions,
            order_instructions,
            limit,
            offset)
        print(query)

        results_raw = self.__cursor.execute(query)

        columns = self.__columns
        if len(columns) == 0:
            columns = self.__table.get_columns()

        results_column_names = list(map(lambda x: x.name, columns))

        self.__results = self.__format_results(results_raw, results_column_names)

    @staticmethod
    def __format_results(results_raw, column_names):
        results = []
        for row_raw in results_raw:
            row = {}
            for column_index in range(len(row_raw)):
                column_name = column_names[column_index]
                row[column_name] = row_raw[column_index]
            results.append(row)
        return results

    def __iter__(self):
        if not self.__is_executed:
            self.__execute()
        return self.__results.__iter__()

    def __next__(self):
        return self.__results.__next__()

    def __str__(self):
        result_strings = list(map(lambda x: str(x), self))
        return "[{0}]".format(", ".join(result_strings))

    def __len__(self):
        if not self.__is_executed:
            self.__execute()
        return len(self.__results)

    def __getitem__(self, item):
        if not self.__is_executed:
            self.__execute()
        return self.__results[item]
