import unittest
from kvdb.kvdb import kv_set, kv_get, kv_del


class TestKVDB(unittest.TestCase):
    def setUp(self):
        self.test_kvdb = {}
        self.test_key = "a"
        self.test_value = 1
        self.test_value_updated = 10
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
    

