from pool_dict import PoolDict
from pool_queue import PoolQueue
from pool_redis import RedisPool


class PoolFactory:
    @staticmethod
    def create_pool(key_attr: str, pool_type: str, **kwargs):
        if pool_type == "dict":
            return PoolDict(key_attr)
        elif pool_type == "queue":
            return PoolQueue()
        elif pool_type == "redis":
            return RedisPool(key_attr, **kwargs)
        else:
            raise ValueError(f"Pool неизвестен")
