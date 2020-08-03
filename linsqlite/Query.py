import types


class Query:

    def __init__(self, table):
        self.__is_executed = False
        self.__table = table
        self.__statements = []

    def select(self, predicate):
        assert isinstance(predicate, types.LambdaType)
        assert not self.__is_executed

        column_metadata = predicate(self.__table)
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
