import unittest
from pool_dict import PoolDict

class TestPoolLength(unittest.TestCase):

    def setUp(self):
        self.pool = PoolDict('id')
        self.objects = [
            {'id': 1, 'name': 'obj1'},
            {'id': 2, 'name': 'obj2'},
            {'id': 3, 'name': 'obj3'},
        ]
        self.pool.set(self.objects)

    def test_length(self):
        self.assertEqual(self.pool.length, 3)