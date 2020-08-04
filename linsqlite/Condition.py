from enum import Enum


class ConditionType(Enum):
    GREATER_THAN = ">"
    LESS_THAN = "<"
    EQUALS = "IS"
    NOT_EQUALS = "IS NOT"


class Condition:

    def __init__(self, column, condition_type, value):
        assert isinstance(condition_type, ConditionType)

        self.column = column
        self.type = condition_type
        self.value = value

    def __str__(self):
        column_name = self.column.name
        operator = self.type.value

        value = self.value
        if value is str:
            value = "'{0}'".format(self.value)
        else:
            value = str(value)

        return "{0} {1} {2}".format(column_name, operator, value)
