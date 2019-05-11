from unittest import TestCase, main
from hash_table import HashTable


class HashTest(TestCase):
    def setUp(self):
        self.test1 = HashTable(10)

    def test_type(self):
        self.assertIsInstance(self.test1, HashTable)

    def test_add(self):
        self.assertEqual(self.test1.insert("key", "var"), None)

    def test_search(self):
        self.test1.insert("key", "val")
        self.assertEqual(self.test1.search("key"), "val")


if __name__ == "__main__":
    main()
