import unittest

from lab6.ijones import find_ways_count


class FindWaysCountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix1 = [
            ["a", "a", "a"],
            ["c", "a", "b"],
            ["d", "e", "f"]
        ]
        self.matrix2 = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]
        self.matrix3 = [
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"]
        ]

    def test_first_case(self):
        self.assertEqual(find_ways_count(self.matrix1, 3, 3), 5)

    def test_second_case(self):
        self.assertEqual(find_ways_count(self.matrix2, 10, 1), 4)

    def test_third_case(self):
        self.assertEqual(find_ways_count(self.matrix3, 7, 6), 201684)


if __name__ == '__main__':
    unittest.main()
