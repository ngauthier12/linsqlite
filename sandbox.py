from linsqlite.Connection import Connection


if __name__ == "__main__":
    connection = Connection("test.sqlite")
    test1 = connection.cars.select(lambda x: (x.make, x.model)).where(lambda x: x.year > 2015)
    print(test1[1]["make"])

    data = connection.cars.where(lambda x: x.year > 2015)
    print(data)

