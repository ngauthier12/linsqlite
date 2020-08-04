from linsqlite.Condition import *


class Column:

    def __init__(self, column_name):
        assert isinstance(column_name, str), "Expecting column_name to be of type str"
        self.name = column_name

    def __gt__(self, other):
        return Condition(self, ConditionType.GREATER_THAN, other)

    def __lt__(self, other):
        return Condition(self, ConditionType.LESS_THAN, other)

    def __eq__(self, other):
        return Condition(self, ConditionType.EQUALS, other)
