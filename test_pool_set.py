import unittest
from pool_dict import PoolDict

class TestPoolSet(unittest.TestCase):

    def setUp(self):
        self.pool = PoolDict('id')

    def test_set(self):
        objects = [
            {'id': 1, 'name': 'obj1'},
            {'id': 2, 'name': 'obj2'},
            {'id': 3, 'name': 'obj3'},
        ]
        self.pool.set(objects)
        self.assertEqual(self.pool.length, 3)
        self.assertEqual(self.pool.list(), objects)