class PoolDict:
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
    def __init__(self, key_attr: str):
        self._pool = {}
        self._key_attr = key_attr

    @property
    def length(self):
        return len(self._pool)

    def list(self, filter_string: [str] = None, filter_attr: str = None):
        """
        Получение списка объектов.
        """
        result = []
        for obj in self._pool.values():
            if not filter_string or not filter_attr or obj[filter_attr] in filter_string:
                result.append(obj)
        return result

    def set(self, objects):
        """
        Добавление объекта в пул.
        """
        for obj in objects:
            key = obj[self._key_attr]
            self._pool[key] = obj

    def pop(self, key):
        """
        Удаляет и возвращает объект из пула по его ключу.
        """
        result = self._pool.pop(key, None)
        return result

    def get(self, key):
        """
        Получение объекта по ключу.
        """
        result = self._pool.get(key, None)
        return result

    def delete(self, keys):
        """
        Удаление объектов.
        """
        for key in keys:
            self._pool.pop(key, None)

