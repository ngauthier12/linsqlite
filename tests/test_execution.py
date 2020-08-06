from tests.test_base import TestBase


class TestExecution(TestBase):

    def test_execute_str(self):
        expected = "[{'make': 'subaru'}]"
        result = self.connection.cars.select(lambda x: x.make).where(lambda x: x.year == 2017)
        self.assertEqual(expected, str(result))

    def test_execute_len(self):
        result = self.connection.cars.select(lambda x: x.make).where(lambda x: x.year != 2017)
        self.assertEqual(len(result), 2)

    def test_execute_iter(self):
        results = self.connection.cars.select(lambda x: x.make).where(lambda x: x.year != 2017)

        expected = [{"make": "chevrolet"}, {"make": "toyota"}]
        counter = 0
        for result in results:
            self.assertEqual(expected[counter], result)
            counter += 1

    def test_execute_get_item(self):
        result = self.connection.cars.select(lambda x: x.make).where(lambda x: x.year != 2017)
        self.assertEqual(result[1]["make"], "toyota")

    def test_double_execution(self):
        result = self.connection.cars.select(lambda x: x.make).where(lambda x: x.year != 2017)
        self.assertEqual(result[1]["make"], "toyota")
        self.assertRaises(AssertionError, result.execute)
