import functools
import uuid

import functools
import uuid


class SingletonManager(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.id = uuid.uuid4()
        return cls._instance

class SingleLruManager():
    def __init__(self):
        self.id = uuid.uuid4()

    @classmethod
    @functools.lru_cache
    def get(cls):
        return Manager()


class Manager():
    def __init__(self):
        self.id = uuid.uuid4()


@functools.lru_cache
def get_manager():
    return Manager()


if __name__ == '__main__':

    for _ in range(3):
        manager = SingletonManager.instance()
        print(manager.id)
