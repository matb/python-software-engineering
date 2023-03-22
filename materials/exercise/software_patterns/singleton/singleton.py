
class Singleton(object):
    @staticmethod
    def instance():
        return Singleton()


def main() -> None:
    foo = Singleton.instance()
    bar = Singleton.instance()

    assert foo == bar


if __name__ == '__main__':
    main()
