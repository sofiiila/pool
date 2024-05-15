import unittest
from redis import Redis
from pool_redis import RedisPool
from test_model import TestModel


class TestRedisPoolGet(unittest.TestCase):

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

    def test_get(self):
        obj = self.pool.get('obj1:1')
        self.assertIsInstance(obj, TestModel)
        self.assertEqual(obj.name, 'obj1')
        self.assertEqual(obj.value, 1)

        obj = self.pool.get('obj2:2')
        self.assertIsInstance(obj, TestModel)
        self.assertEqual(obj.name, 'obj2')
        self.assertEqual(obj.value, 2)

        obj = self.pool.get('obj3:3')
        self.assertIsInstance(obj, TestModel)
        self.assertEqual(obj.name, 'obj3')
        self.assertEqual(obj.value, 3)

        obj = self.pool.get('nonexistent_key')
        self.assertIsNone(obj)


if __name__ == '__main__':
    unittest.main()