from linsqlite.Connection import Connection


if __name__ == "__main__":
    connection = Connection("test.sqlite")
    makes = connection.cars.select(lambda x: (x.make, x.model)).where(lambda x: x.year > 2015)
    print(makes)

    data = connection.cars.where(lambda x: x.year > 2015)
    print(data)

