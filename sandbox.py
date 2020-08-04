from linsqlite.Connection import Connection


if __name__ == "__main__":
    connection = Connection("test.sqlite")
    makes = connection.cars.select(lambda x: (x.make, x.model))
    print(makes)

