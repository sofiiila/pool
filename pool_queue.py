import multiprocessing

class PoolQueue:
    """
    Класс для хранения объектов.

    Инициализация:

    Pool(key_attr: str). key_attr - название атрибута, который будет являться ключом.

    Методы:

    - list(filter_string: [str] = None, filter_attr: str = None) - возвращает список объектов.
                                                                   filter_string - список фильтров, которые
                                                                   нужно получить.

    - delete(keys: [str]) - удаляет объекты. keys - список ключей удаления.

    - set(pool_objects: [Any]) - Добавляет задачи в список. pool_objects - список объектов.

    - get(key: str) - Получение объекта по ключу. key - ключ объекта.

    """
    def __init__(self):
        self._pool = multiprocessing.Queue()
        self._key_attr = key_attr

    @property
    def length(self):
        return self._pool.qsize()

    def list(self, filter_string: [str] = None, filter_attr: str = None):
        """
        Получение списка объектов.
        """
        local_memory = []
        result = []
        queue_size = self._pool.qsize()
        for _ in range(queue_size):
            obj = self._pool.get(timeout=10)
            local_memory.append(obj)
            if not filter_string or not filter_attr or getattr(obj, filter_attr) in filter_string:
                result.append(obj)
        for memory_object in local_memory:
            self._pool.put(memory_object)
        return result

    def set(self, objects):
        """
        Добавление объекта в пул.
        """
        for obj in objects:
            self._pool.put(obj)

    def pop(self, key):
        """
        Получение объекта по ключу.
        """
        result = None
        local_memory = []
        queue_size = self._pool.qsize()
        for _ in range(queue_size):
            try:
                result_get = self._pool.get(timeout=10)
                if result_get.key == key:
                    result = result_get
                else:
                    local_memory.append(result_get)
            except Empty:
                pass
        for memory_object in local_memory:
            self._pool.put(memory_object)
        return result

    def get(self, key):
        """
        Получение объекта по ключу.
        """
        result = None
        local_memory = []
        queue_size = self._pool.qsize()
        for _ in range(queue_size):
            try:
                result_get = self._pool.get(timeout=10)
                if result_get.key == key:
                    result = result_get
                local_memory.append(result_get)
            except Empty:
                pass
        for memory_object in local_memory:
            self._pool.put(memory_object)
        return result

    def delete(self, key):
        """
        Удаление объектов.
        """
        local_memory = []
        queue_size = self._pool.qsize()
        for _ in range(queue_size):
            try:
                result_get = self._pool.get(timeout=10)
                if result_get.key != key:
                    local_memory.append(result_get)
            except Empty:
                pass

        for memory_object in local_memory:
            self._pool.put(memory_object)
