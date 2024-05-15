import unittest
from pool_dict import PoolDict

class TestPoolGet(unittest.TestCase):

    def setUp(self):
        self.pool = PoolDict('id')
        self.objects = [
            {'id': 1, 'name': 'obj1'},
            {'id': 2, 'name': 'obj2'},
            {'id': 3, 'name': 'obj3'},
        ]
        self.pool.set(self.objects)

    def test_get(self):
        self.assertEqual(self.pool.get(1), self.objects[0])
