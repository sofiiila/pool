import unittest
from redis import Redis
from pool_redis import RedisPool
from test_model import TestModel


class TestRedisPoolList(unittest.TestCase):

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

    def test_list(self):
        objects = self.pool.list()
        self.assertEqual(len(objects), len(self.test_objects))
        for obj, expected_obj in zip(objects, self.test_objects):
            self.assertIsInstance(obj, TestModel)
            self.assertEqual(obj.name, expected_obj.name)
            self.assertEqual(obj.value, expected_obj.value)


if __name__ == '__main__':
    unittest.main()
