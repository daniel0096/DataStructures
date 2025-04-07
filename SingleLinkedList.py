from typing import Optional, TypeVar, Generic, Iterator, Union
import DataUtils

T = TypeVar('T')

class SingleLinkedList(Generic[T]):
    """
    Generic single linked list implementation.

    Attributes:
        _size int: Number of elements in the linked list.
        _head (Optional[LinkedListNode[T]]): refers to the first node of the list.
    """

    class LinkedListNode(Generic[T]):
        """
        Represents single node in a linked list datastructure.

        Attributes:
            item (T): The value stored in the node.
            nextNode (Optional[LinkedListNode[T]]): Reference to the next node in the list.
        """

        def __init__(self, item_data: T):
            """
            Initializes LinkedListNode in the linked list.

            :param item_data: Data to store into a node.
            :type item_data: T 
            """

            self.item: T = item_data
            self.nextNode: Optional['LinkedListNode[T]'] = None

    def __init__(self):
        """
        Initializes empty SingleLinkedList.
        """

        self._size: int = 0
        self._head: Optional[LinkedListNode[T]] = None

    def __repr__(self) -> str:
        """
        Returns a text representation of linked list

        :returns: A string showing the items in the list, separated by arrows.
        :rtype: str
        """
        return ' -> '.join(str(x) for x in self)  

    def __len__(self) -> int:
        """
        Returns actual length of single linked list

        :returns: Size of the list.
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Iterates through 'self', meaning exact values held by existing nodes.

        :return: Iterated 'self'
        :rtype: Iterator[T]
        """

        current = self._head
        while current:
            yield current.item
            current = current.nextNode

    def __contains__(self, item: T) -> bool:
        """
        Checks if the given item exists inside of the existing node.

        :return: True if the item inside of the node exists, otherwise False
        :rtype: bool
        """
        return self.find_by_value(item) is not None

    def __eq__(self, next_linked_list: object) -> bool:
        """
        Checks if current - self linked list is equal to another linked list.

        :param next_linked_list: Another linked list.
        :type next_linked_list: object
        :return: True if current linked list is equal to another, otherwise False
        :rtype: bool
        """

        if not isinstance(next_linked_list, SingleLinkedList):
            return False
        
        if len(self) != len(next_linked_list):
            return False

        for value_a, value_b in zip(self, next_linked_list):
            if value_a != value_b:
                return False
        return True

    @DataUtils.requires_not_null
    def __getitem__(self, data: Union[int, slice, None]) -> T:
        """
        Returns an item held by linked list node based on given index.

        :param index: Index of the node.
        :type int
        :return: Item held by the node at the given index.
        :rtype: T
        """
        if isinstance(data, slice):
            start, stop, step = data.indices(self._size)
            result = []
            current = self._head
            i = 0
            while current and i < stop:
                if i >= start and (i - start) % step == 0:
                    result.append(current.item)
                current = current.nextNode
                i += 1
            return result
        elif isinstance(data, int):
            self._validate_index(data)
 
            current = self._head

            for _ in range(data):
                current = current.nextNode

            return current.item
        else:
            raise DataUtils.LinkedListException('Expected int or slice.')

    @DataUtils.requires_not_null
    def __setitem__(self, index: int, item: T):
        """
        Sets the item at the specified index in the linked list.

        :param index: The index of the node that will be modified.
        :type index: int
        :param item: New value to assign to the node.
        :type item: T
        :raises LinkedListException: If the index is out of range or if arguments are null.
        """

        self._validate_index(index)

        current = self._head

        for _ in range(index):
            current = current.nextNode
        current.item = item

    def __delitem__(self, index: int):
        """
        Deletes an item at the specified index.


        :param index: Index of the node to delete.
        :type index: int
        """
        self.pop_at(index)

    def __bool__(self) -> bool:
        """
        Checks if a linked list exists.

        :rtype: bool
        """
        return not self.is_empty()

    @DataUtils.requires_not_null
    def at(self, index: int) -> 'LinkedListNode[T]':
        """
        Returns node at the specified index.

        :param index: Index of the node to get.
        :type index: int
        :return: Actual node at the given index.
        :rtype: T
        :raises LinkedListException: If the index is invalid or null.
        """

        self._validate_index(index)

        current = self._head

        for _ in range(index):
            current = current.nextNode
        return current

    @DataUtils.requires_not_null
    def find_by_value(self, value: T) -> Optional[int]:
        """
        Finds the index of the searched value in the list.

        :param value: Value to search for in the list.
        :type value: T
        :return: Index of the value if it was found, otherwise None.
        :rtype: Optional[int]
        """

        index = 0
        current = self._head

        while current:
            if value == current.item:
                return index
            current = current.nextNode
            index += 1
        return None

    @DataUtils.requires_not_null
    def push_back(self, element: T):
        """
        Appends a new element at the end of the linked list.

        :param element: Value to be added to the end of the list.
        :type element: T
        """

        new_node = self.LinkedListNode(element)

        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.nextNode:
                current = current.nextNode
            current.nextNode = new_node

        self._size += 1

    def insert_at(self, element: T, index: int):
        """
        Inserts a new element at the given index.

        :param element: Value to be inserted.
        :type element: T
        :param index: Index where the new element should be placed.
        :type index: int
        :raises LinkedListException: If index is out of range.
        """

        self._validate_index(index)

        if index == self._size:
            self.push_back(element)
            return

        new_node = self.LinkedListNode(element)

        if self.is_empty():
            self._head = new_node
        else:
            current = self._head

            for _ in range(index - 1):
                current = current.nextNode
            new_node.nextNode = current.nextNode
            current.nextNode = new_node

        self._size += 1

    @DataUtils.requires_non_empty
    def pop_back(self):
        """
        Removes the last element from the linked list.

        :raises LinkedListException: If the list is empty.
        """

        pre_node = self._head

        # get index at pre - last index & cut the last node
        if self._size == 1:
            self._head = None
        else:
            pre_node = self._head
            for _ in range(self._size - 2):
                pre_node = pre_node.nextNode
            pre_node.nextNode = None
        self._size -= 1

    @DataUtils.requires_non_empty
    def pop_at(self, index: int):
        """
        Removes the element at the given index.

        :param index: Index of the node to remove.
        :type index: int
        :raises LinkedListException: If the list is empty or index is invalid.
        """

        self._validate_index(index)

        if index == 0:
            self._head = self._head.nextNode
        else:
            prev = self._head
            for _ in range(index - 1):
                prev = prev.nextNode
            target = prev.nextNode
            prev.nextNode = target.nextNode
        self._size -= 1

    def extend(self, next_linked_list: 'SingleLinkedList[T]'):
        """
        Pushes all elements from another linked list to the end of the current list.

        :param next_linked_list: Another linked list to push.
        :type next_linked_list: SingleLinkedList[T]
        """

        for item in next_linked_list:
            self.push_back(item)

    def copy(self) -> 'SingleLinkedList[T]':
        """
        Creates a copy of the linked list.

        :return: A new instance of SingleLinkedList with copied elements.
        :rtype: SingleLinkedList[T]
        """

        new_list = SingleLinkedList[T]()

        for item in self:
            new_list.push_back(item)

        return new_list

    def reverse(self):
        """
        Reverses the linked list.
        """

        prev = None
        current = self._head

        while current:
            next_node = current.nextNode
            current.nextNode = prev
            prev = current
            current = next_node

        self._head = prev

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.

        :return: True if the list is empty, otherwise False.
        :rtype: bool
        """
        return self._size == 0

    def clear(self):
        """
        Removes all elements from the linked list.
        """
        self._head = None
        self._size = 0

    def to_list(self) -> list[T]:
        """
        Converts the linked list to a standard Python list.

        :return: List containing all elements from the linked list.
        :rtype: list
        """
        return list(self)

    def _validate_index(self, index: int):
        """
        Validates if the given index is in range.

        :param index: Index to validate.
        :type index: int
        :raises LinkedListException: If index is out of bounds.
        """

        if (index >= self._size or index < 0):
            raise DataUtils.LinkedListException(f'Invalid index, expected 0-{self._size}, got {index}')