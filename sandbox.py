from linsqlite.Connection import Connection


if __name__ == "__main__":
    connection = Connection("test.sqlite")
    table = connection.get_table("cars")
    print(table)
