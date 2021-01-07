import unittest
from kvdb.kvdb import kv_set, kv_get, kv_del, kv_incr, kv_incrby, kv_execute_multiline, kv_compact


class TestKVDB(unittest.TestCase):
    def setUp(self):
        self.test_kvdb = {}
        self.test_key = "a"
        self.test_new_key = "counter"
        self.test_value = 1
        self.test_value_updated = 10
        self.test_incr_value_by = 11
        self.initial_kvdb_length = len(self.test_kvdb)
        self.multiline_commands = [
            "MULTI",
            "SET {} 1".format(self.test_key),
            "INCRBY {} 9".format(self.test_key),
            "INCR {}".format(self.test_new_key) 
        ]

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

    def test_multiline_exec(self):
        multiline_command = self.multiline_commands + ["EXEC"]
        res = kv_execute_multiline(self.test_kvdb, multiline_command)

        self.assertEqual(10, res.get(self.test_key))
        self.assertEqual(1, res.get(self.test_new_key))

    def test_multiline_discard(self):
        multiline_command = self.multiline_commands + ["DISCARD"]
        res = kv_execute_multiline(self.test_kvdb, multiline_command)

        self.assertEqual(None, res.get(self.test_new_key))

    def test_kv_compact(self):
        res = kv_set(self.test_kvdb, **{"key": self.test_key, "value": self.test_value})
        res = kv_incrby(self.test_kvdb, **{"key": self.test_key, "incr_by": self.test_incr_value_by})
        res = kv_incr(self.test_kvdb, **{"key": self.test_key})
        res = kv_incr(self.test_kvdb, **{"key": self.test_new_key})
        res = kv_compact(self.test_kvdb)

        expected_output = [
            "SET {} 13".format(self.test_key),
            "SET {} 1".format(self.test_new_key)
        ]

        self.assertEqual(expected_output, res)
