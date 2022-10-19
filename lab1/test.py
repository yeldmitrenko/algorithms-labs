import unittest
from heap_sort import heap_sort
from copy import deepcopy


class TestHeapSort(unittest.TestCase):
    def setUp(self) -> None:
        self.array_example = [1, 2, 56, 45, -9, 78, 11]
        self.array_sorted_asc = [-9, 1, 2, 11, 45, 56, 78]
        self.array_sorted_desc = [78, 56, 45, 11, 2, 1, -9]

    def test_sort_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_example), "asc"), self.array_sorted_asc)

    def test_sort_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_example), "desc"), self.array_sorted_desc)

    def test_sort_asc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_sorted_asc), "asc"), self.array_sorted_asc)

    def test_sort_asc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_sorted_asc), "desc"), self.array_sorted_desc)

    def test_sort_desc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_sorted_desc), "asc"), self.array_sorted_asc)

    def test_sort_desc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_sorted_desc), "desc"), self.array_sorted_desc)
