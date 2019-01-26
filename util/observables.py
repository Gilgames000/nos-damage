from abc import ABC, abstractmethod
from collections import Iterable


class Observable(ABC, Iterable):
    def __init__(self):
        self._observers = []
        self._changed = False

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __contains__(self, item):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def add_observer(self, observer):
        self._observers.append(observer)

    def delete_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def delete_observers(self):
        self._observers.clear()

    def set_changed(self):
        self._changed = True

    def clear_changed(self):
        self._changed = False

    def has_changed(self):
        return self._changed

    def notify_observers(self, args=None):
        for observer in self._observers:
            observer.update(self, args)

    def count_observers(self):
        return len(self._observers)


class ObservableList(Observable):
    def __init__(self, items=None):
        super().__init__()
        self._list = items if items else []

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        if isinstance(index, slice):
            item = ObservableList(list(self._list[index]))
        else:
            item = self._list[index]

        return item

    def __eq__(self, other):
        if not isinstance(other, ObservableList):
            return NotImplemented
        return self._list == other._list

    def __ne__(self, other):
        if not isinstance(other, ObservableList):
            return NotImplemented
        return self._list != other._list

    def __reversed__(self):
        return ObservableList(list(reversed(self._list)))

    def __add__(self, other):
        if not isinstance(other, ObservableList):
            return NotImplemented
        return ObservableList(self._list + other._list)

    def __iter__(self):
        return iter(self._list)

    def __contains__(self, item):
        return item in self._list

    def index(self, item):
        return self._list.index(item)

    def append(self, item) -> None:
        self._list.append(item)

    def extend(self, items: Iterable) -> None:
        self._list.extend(items)

    def insert(self, index, item) -> None:
        self._list.insert(index, item)

    def remove(self, item) -> None:
        self._list.remove(item)

    def pop(self) -> None:
        self._list.pop()

    def clear(self) -> None:
        self._list.clear()

    def count(self, item) -> int:
        return self._list.count(item)

    def sort(self, key=None, reverse=False) -> None:
        self._list.sort(key=key, reverse=reverse)
