from enum import Enum


class OrderDirection(Enum):
    ASCENDING = "ASC"
    DESCENDING = "DESC"


class OrderInstruction:

    def __init__(self, column, direction):
        assert isinstance(direction, OrderDirection), "direction is expected to be an OrderDirection"

        self.column = column
        self.direction = direction

    def __str__(self):
        column_name = self.column.name
        direction = self.direction.value

        return "{0} {1}".format(column_name, direction)
