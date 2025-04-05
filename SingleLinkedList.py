from typing import Callable, Any, Optional
import DataUtils

class SingleLinkedList(object):
    class LinkedListNode(object):
        def __init__(self, item_data: Any):
            self.item = item_data
            self.nextNode: Optional['LinkedListNode'] = None

    def __init__(self):
        self._size: int = 0
        self._head: Optional[LinkedListNode] = None

    def __repr__(self):
        pass

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.item
            current = current.nextNode

    def __getitem__(self, subscript) -> Optional[Any]:
        if isinstance(subscript, slice):
            pass

    def __setitem__(self, item: Any):
        pass

    @DataUtils.requires_not_null
    def at(self, index: int) -> Optional[int]:
        """
        at
        """
        pass

    @DataUtils.requires_not_null
    def find_by_value(self, ) -> Optional[Any]:
        pass

    def push_back(self, element: Any):
        pass

    def insert_at(self, element: Any, index: int):
        pass

    def pop_front(self):
        pass

    def pop_at(self, index: int):
        pass

    def reverse(self):
        pass

    @property
    def isEmpty(self) -> bool:
        return self.size == 0

