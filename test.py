import unittest

from lab7.rabin_karp import rabin_karp_search


class RabinKarpTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_text1 = "AAA NN MM LL K AA"
        self.test_pattern1 = "AA"
        self.benchmark_positions_array1 = [0, 1, 15]

        self.test_pattern2 = "LLN"
        self.test_text2 = "BBCLLNMNLLN"
        self.benchmark_positions_array2 = [3, 8]

    def test_rabin_karp_search_1(self):
        pattern_positions = rabin_karp_search(self.test_text1, self.test_pattern1)
        self.assertEqual(pattern_positions, self.benchmark_positions_array1)

    def test_rabin_karp_search_2(self):
        pattern_positions = rabin_karp_search(self.test_text2, self.test_pattern2)
        self.assertEqual(pattern_positions, self.benchmark_positions_array2)


if __name__ == '__main__':
    unittest.main()
