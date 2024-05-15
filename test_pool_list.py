import unittest
from pool_dict import PoolDict

class TestPoolList(unittest.TestCase):

    def setUp(self):
        self.pool = PoolDict('id')
        self.objects = [
            {'id': 1, 'name': 'obj1'},
            {'id': 2, 'name': 'obj2'},
            {'id': 3, 'name': 'obj3'},
        ]
        self.pool.set(self.objects)

    def test_list(self):
        self.assertEqual(self.pool.list(), self.objects)

    def test_list_filter(self):
        self.assertEqual(self.pool.list(filter_string=['obj1', 'obj2'], filter_attr='name'),
                         [self.objects[0], self.objects[1]])

