import json
import unittest
from redis import Redis
from pool_redis import RedisPool
from test_model import TestModel


class TestRedisPoolSet(unittest.TestCase):

    def setUp(self):
        self.redis = Redis()
        self.redis.flushdb()
        self.pool = RedisPool(host='localhost', port=6379, key='test_key', obj_class=TestModel)
        self.test_objects = [
            TestModel(name='obj1', value=1),
            TestModel(name='obj2', value=2),
            TestModel(name='obj3', value=3)
        ]

    def tearDown(self):
        self.redis.flushdb()

    def test_set(self):
        self.pool.set(self.test_objects)

        for obj in self.test_objects:
            task_obj = self.redis.hget(self.pool.key, obj.key).decode()
            self.assertEqual(task_obj, json.dumps(obj.dict()))


if __name__ == '__main__':
    unittest.main()