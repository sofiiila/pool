import unittest
from redis import Redis
from pool_redis import RedisPool
from test_model import TestModel


class TestRedisPoolDelete(unittest.TestCase):

    def setUp(self):
        self.redis = Redis()
        self.redis.flushdb()
        self.pool = RedisPool(host='localhost', port=6379, key='test_key', obj_class=TestModel)
        self.test_objects = [
            TestModel(name='obj1', value=1),
            TestModel(name='obj2', value=2),
            TestModel(name='obj3', value=3)
        ]
        self.pool.set(self.test_objects)

    def tearDown(self):
        self.redis.flushdb()

    def test_delete(self):
        self.pool.delete('obj1:1')
        self.assertIsNone(self.pool.get('obj1:1'))

        self.pool.delete('obj2:2')
        self.assertIsNone(self.pool.get('obj2:2'))

        self.pool.delete('obj3:3')
        self.assertIsNone(self.pool.get('obj3:3'))

        self.assertEqual(self.pool.list(), [])


if __name__ == '__main__':
    unittest.main()