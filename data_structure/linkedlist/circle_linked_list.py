from typing import Any


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def insert(self, index: int, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            else:
                temp = self.head
                for _ in range(index):
                    temp = temp.next

                new_node.next = temp.next
                temp.next = new_node

    def delete(self, data) -> bool:
        if self.head is None:
            return False
        temp = self.head
        prev = None
        is_find = False
        for _ in range(self.get_length()):
            if temp.data == data:
                is_find = True
                break
            prev = temp
            temp = temp.next
        if is_find is False:
            print("Not found data in linked list")
            return False
        prev.next = temp.next
        return True

    def exchange_first_and_last(self) -> None:
        data = self.head.data
        self.head.data = self.tail.data
        self.tail.data = data

    def get_length(self) -> int:
        visited = []
        temporary = self.head
        result = 0
        while temporary is not None:
            if id(temporary) not in visited:
                visited.append(id(temporary))
            else:
                break
            result += 1
            temporary = temporary.next
        return result

    def is_empty(self) -> bool:
        return self.head is None

    def traversal_linkedlist(self) -> str:
        visited = []
        temporary = self.head
        result = []
        while temporary is not None:
            if id(temporary) not in visited:
                visited.append(id(temporary))
            else:
                break
            result.append(str(temporary.data))
            temporary = temporary.next
        return " -> ".join(result)


if __name__ == "__main__":
    ll = CircularLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.insert(2, 99)
    ll.insert(0, 77)
    ll.insert(0, 55)
    print("Exchange first and last nodes")
    ll.exchange_first_and_last()
    print("Traversal Linked list")
    print(ll.traversal_linkedlist())
    print("Delete Nodes")
    ll.delete(1)
    ll.delete(2)
    print("Traversal Linked list")
    print(ll.traversal_linkedlist())
    print("Get length")
    print(ll.get_length())
