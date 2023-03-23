
class Singleton(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod # a classmethod is a static method on the object that receives the context of the class. @staticmethod does not have any information about the class it gets called on
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


def main() -> None:
    foo = Singleton.instance()
    bar = Singleton.instance()

    assert foo == bar

if __name__ == '__main__':
    main()
