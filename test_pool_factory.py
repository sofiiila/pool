import unittest

from pool_dict import PoolDict
from pool_factory import PoolFactory
from pool_queue import PoolQueue

class TestPoolFactory(unittest.TestCase):

    def test_create_pool_dict(self):
        pool = PoolFactory.create_pool(key_attr='id', multiprocess=False)
        self.assertIsInstance(pool, PoolDict)

    def test_create_pool_queue(self):
        pool = PoolFactory.create_pool(key_attr='id', multiprocess=True)
        self.assertIsInstance(pool, PoolQueue)

