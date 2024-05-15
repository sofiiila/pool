from pool_dict import PoolDict
from pool_queue import PoolQueue


class PoolFactory:
    @staticmethod
    def create_pool(key_attr: str, multiprocess: bool = False):
        if multiprocess:
            return PoolQueue()
        else:
            return PoolDict(key_attr)
