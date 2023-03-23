class SingletonAnnotation:
    """
    This should be used as a decorator to the class that should be a singleton.
    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.
    To get the singleton instance, use the `instance` method. 
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        if not hasattr(self, '_instance'):
            self._instance = self._decorated()

        return self._instance

    # see here for a good explanation of __call__ https://www.geeksforgeeks.org/__call__-in-python/
    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@SingletonAnnotation
class Singleton(object):
    pass


def main() -> None:
    foo = Singleton.instance()
    bar = Singleton.instance()

    assert foo == bar


if __name__ == '__main__':
    main()
