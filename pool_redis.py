from __future__ import annotations
import json
from typing import Any, List
import redis
from pydantic import BaseModel


class RedisPool:

    def __init__(self, host: str, port: int, key: str, obj_class: Any, redis_client: redis.Redis | None = None):
        self.key = key
        self.obj_class = obj_class
        if redis_client is not None:
            self.redis = redis_client
        else:
            self.redis = redis.Redis(host=host, port=port)
        print(self.redis)

    def list(self) -> List[Any]:
        keys = self.redis.hkeys(self.key)
        objects = []
        for key in keys:
            task_obj = self.redis.hget(self.key, key)
            obj = self.obj_class(**json.loads(task_obj)) if task_obj else None
            objects.append(obj)
        return objects

    def set(self, objects: [BaseModel]) -> None:
        for obj in objects:
            task_obj = json.dumps(obj.dict())
            self.redis.hset(self.key, obj.key, task_obj)

    def get(self, key) -> Any:
        task_obj = self.redis.hget(self.key, key)
        return self.obj_class(**json.loads(task_obj)) if task_obj else None

    def pop(self, key) -> Any:
        task_obj = self.redis.hget(self.key, key)
        value = self.obj_class(**json.loads(task_obj)) if task_obj else None
        self.redis.hdel(self.key, key)
        return value

    def delete(self, key) -> None:
        self.redis.hdel(self.key, key)


