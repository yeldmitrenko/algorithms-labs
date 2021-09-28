import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.table = HashTable()

    def test_insert(self):
        self.assertEqual(self.table.insert("key1", "value1"), [("key1", "value1")])

    def test_get(self):
        self.table.insert("key1", "value1")
        self.assertEqual(self.table.get("key1"), [("key1", "value1")])

    def test_delete(self):
        self.table.insert("key1", "value1")
        self.assertEqual(self.table.delete("key1"), "key1")
