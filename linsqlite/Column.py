

class Column:

    def __init__(self, column_name):
        assert isinstance(column_name, str), "Expecting column_name to be of type str"
        self.name = column_name
