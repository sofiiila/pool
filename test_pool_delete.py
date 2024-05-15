import unittest
from pool_dict import PoolDict

class TestPoolDelete(unittest.TestCase):

    def setUp(self):
        self.pool = PoolDict('id')
        self.objects = [
            {'id': 1, 'name': 'obj1'},
            {'id': 2, 'name': 'obj2'},
            {'id': 3, 'name': 'obj3'},
        ]
        self.pool.set(self.objects)

    def test_delete(self):
        self.pool.delete([1, 2])
        self.assertEqual(self.pool.length, 1)
        self.assertEqual(self.pool.list(), [self.objects[2]])