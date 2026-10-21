import unittest

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_get_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 100)

        self.assertEqual(cache.get(1), 100)

    def test_get_missing_key(self):
        cache = LRUCache(2)

        self.assertEqual(cache.get(5), -1)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 100)
        cache.put(1, 200)

        self.assertEqual(cache.get(1), 200)

    def test_evict_least_recently_used(self):
        cache = LRUCache(2)
        cache.put(1, 100)
        cache.put(2, 200)
        cache.get(1)
        cache.put(3, 300)

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 100)
        self.assertEqual(cache.get(3), 300)

    def test_zero_capacity(self):
        cache = LRUCache(0)
        cache.put(1, 100)

        self.assertEqual(cache.get(1), -1)

    def test_negative_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(-1)


if __name__ == "__main__":
    unittest.main()
