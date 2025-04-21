from typing import Optional, TypeVar, Any, Generic, Iterator, Union
import DataUtils

T = TypeVar('T')

class DoublyLinkedList(Generic[T]):
    # container
    class ListNode(Generic[T]):
        def __init__(self, item_content: Any):
            self.nextLink: Optional['ListNode[T]'] = None
            self.prevLink: Optional['ListNode[T]'] = None
            self._item_content = item_content # "Ahoj Iga"

    def __init__(self):
        self.head: Optional[ListNode[T]] = None
        self.tail: Optional[ListNode[T]] = None

        self._size = 0

    def __iter__(self) -> Iterator:
        current = self.head
        
        while current:
            yield current._item_content
            current = current.nextLink

    @DataUtils.requires_not_null
    def __getitem__(self, data: Union[int, slice, None]) -> T:
        # get either index or a range (slice)
        if isinstance(data, int):
            current = self.head
            for _ in range(len(data)):
                current = current.nextLink
            return current._item_content

        elif isinstance(data, slice):
            data = []
            pass

    def __setitem__(self, index: int, item: T):
        new_node = self.ListNode(item)

        for _ in range(index):
            pass

    def __reversed__(self) -> Iterator:
        current = self.tail

        while current:
            yield current._item_content
            current = current.prevLink

    @DataUtils.requires_not_null
    def push_back(self, item: T):
        new_node = self.ListNode(item)

        current = self.head

        if self.is_empty(self):
            current = new_node
            return

        while current.nextLink:
            current = current.nextLink
        current.nextLink = new_node

        self._size += 1

    @DataUtils.requires_non_empty
    def pop_back(self):

        # erase everything
        if self.tail is self.head:
            self.head = self.tail = None
        else:
        # tail of the list is set to 
            self.tail = self.tail.prevLink
            self.tail.nextLink = None

        self._size -= 1

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0