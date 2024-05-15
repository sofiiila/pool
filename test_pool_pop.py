import unittest
from pool_dict import PoolDict

class TestPoolPop(unittest.TestCase):

    def setUp(self):
        self.pool = PoolDict('id')
        self.objects = [
            {'id': 1, 'name': 'obj1'},
            {'id': 2, 'name': 'obj2'},
            {'id': 3, 'name': 'obj3'},
        ]
        self.pool.set(self.objects)

    def test_pop(self):
        self.assertEqual(self.pool.pop(1), self.objects[0])
        self.assertEqual(self.pool.length, 2)
        self.assertEqual(self.pool.list(), [self.objects[1], self.objects[2]])