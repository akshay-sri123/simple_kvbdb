import unittest
from kvdb.kvdb import kv_set, kv_get, kv_del, kv_incr, kv_incrby


class TestKVDB(unittest.TestCase):
    def setUp(self):
        self.test_kvdb = {}
        self.test_key = "a"
        self.test_value = 1
        self.test_value_updated = 10
        self.test_incr_value_by = 11
        self.initial_kvdb_length = len(self.test_kvdb)

    def test_kv_set(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})

        self.assertEqual(1, (len(res) - self.initial_kvdb_length))
        self.assertEqual(self.test_value, self.test_kvdb[self.test_key])
    
    def test_kv_set_update_existing_key(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        self.test_kvdb = kv_set(res, **{"key": self.test_key, "value": self.test_value_updated})

        self.assertEqual(self.test_value_updated, self.test_kvdb[self.test_key])

    def test_kv_get(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_get(self.test_kvdb, **{"key": self.test_key})

        self.assertEqual(self.test_value, res)
    
    def test_kv_get_non_existent_key(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_get(self.test_kvdb, **{"key": "abc"})

        self.assertEqual(None, res)

    def test_kv_del(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_del(self.test_kvdb, **{"key": self.test_key})

        self.assertNotIn(self.test_key, res)
    
    def test_kv_del_non_existent_key(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_del(self.test_kvdb, **{"key": "xyz"})
        
        self.assertEqual(None, res)
    
    def test_kv_incr_new_key(self):
        res = kv_incr(self.test_kvdb, **{"key": self.test_key})

        self.assertEqual(1, res)
        # Now that key has been set, check again
        res = kv_incr(self.test_kvdb, **{"key": self.test_key})
        self.assertEqual(2, res)

    def test_kv_incr_existing_key(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_incr(self.test_kvdb, **{"key": self.test_key})
        
        self.assertEqual(self.test_value + 1, res)

    def test_kv_incrby(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_incrby(self.test_kvdb, **{"key": self.test_key, "incr_by": self.test_incr_value_by})
        
        self.assertEqual(self.test_value + self.test_incr_value_by, res)

    def test_kv_incrby_new_key(self):
        res = kv_incrby(self.test_kvdb, **{"key": self.test_key, "incr_by": self.test_incr_value_by})

        self.assertEqual(self.test_incr_value_by, res)
