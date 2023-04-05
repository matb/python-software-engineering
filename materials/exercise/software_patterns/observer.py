class Observable:

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)


class Observer:

    def __init__(self, observable):
        observable.subscribe(self)

    @staticmethod
    def notify(
            observable,
            *args,
            **kwargs
        ):
        print('Got', args, kwargs, 'From', observable)


if __name__ == '__main__':
    subject = Observable()

    observer1 = Observer(subject)
    observer2 = Observer(subject)

    subject.notify_observers('This is the 1st broadcast',
                             kw='From the Observer')
    subject.unsubscribe(observer2)

    subject.notify_observers('This is the 2nd broadcast',
                             kw='From the Observer')
