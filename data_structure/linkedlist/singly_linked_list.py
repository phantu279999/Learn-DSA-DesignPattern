from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        return " -> ".join([str(item) for item in self])

    def __getitem__(self, index: int) -> Any:
        if not 0 <= index < len(self):
            raise Exception("List index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node
        return None

    def __setitem__(self, index, data: Any) -> None:

        if not 0 <= index < len(self):
            raise ValueError("List index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next_node
        current.data = data

    def insert_tail(self, data: Any):
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any):
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("List index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def print_list(self):
        print(self)

    def delete_head(self) -> Any:
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        if not 0 <= index <= len(self):
            raise IndexError("List index out of range.")
        delete_node = self.head
        if index == 0:
            if self.head:
                self.head = self.head.next_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next_node
            delete_node = temp.next_node
            temp.next_node = temp.next_node.next_node
        return delete_node.data

    def is_empty(self):
        return self.head is None

    def reverse(self):

        prev = None
        current_node = self.head
        while current_node:
            # Store the current node's next node.
            next = current_node.next_node
            # Make the current node's next_node point backwards
            current_node.next_node = prev
            # Make the previous node be the current node
            prev = current_node
            # Make the current node the next_node node (to progress iteration)
            current_node = next

        self.head = prev


# def test_singly_linked_list() -> None:
#     """
#     >>> test_singly_linked_list()
#     """
#     linked_list = LinkedList()
#     assert linked_list.is_empty() is True
#     assert str(linked_list) == ""
#
#     try:
#         linked_list.delete_head()
#         raise AssertionError  # This should not happen.
#     except IndexError:
#         assert True  # This should happen.
#
#     try:
#         linked_list.delete_tail()
#         raise AssertionError  # This should not happen.
#     except IndexError:
#         assert True  # This should happen.
#
#     for i in range(10):
#         assert len(linked_list) == i
#         linked_list.insert_nth(i, i + 1)
#     assert str(linked_list) == " -> ".join(str(i) for i in range(1, 11))
#
#     linked_list.insert_head(0)
#     linked_list.insert_tail(11)
#     assert str(linked_list) == " -> ".join(str(i) for i in range(12))
#
#     assert linked_list.delete_head() == 0
#     assert linked_list.delete_nth(9) == 10
#     assert linked_list.delete_tail() == 11
#     assert len(linked_list) == 9
#     assert str(linked_list) == " -> ".join(str(i) for i in range(1, 10))
#
#     assert all(linked_list[i] == i + 1 for i in range(9)) is True
#
#     for i in range(9):
#         linked_list[i] = -i
#     assert all(linked_list[i] == -i for i in range(9)) is True
#
#     linked_list.reverse()
#     assert str(linked_list) == " -> ".join(str(i) for i in range(-8, 1))



def main():
    from doctest import testmod

    testmod()

    linked_list = LinkedList()
    linked_list.insert_head(input("Inserting 1st at head ").strip())
    linked_list.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    linked_list.insert_tail(input("\nInserting 1st at tail ").strip())
    linked_list.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    print("\nDelete head")
    linked_list.delete_head()
    print("Delete tail")
    linked_list.delete_tail()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nReverse linked list")
    linked_list.reverse()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nString representation of linked list:")
    print(linked_list)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {linked_list[1]}")
    linked_list[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(linked_list)
    print(f"length of linked_list is : {len(linked_list)}")


if __name__ == "__main__":
    main()