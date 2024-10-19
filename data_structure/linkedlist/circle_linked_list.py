class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def traversal_linkedlist(self):
        visited = []
        temporary = self.head
        while temporary is not None:
            if id(temporary) not in visited:
                visited.append(id(temporary))
            else:
                break
            print(temporary.data, end=" ")
            temporary = temporary.next
        print()


if __name__ == "__main__":
    ll = CircularLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.traversal_linkedlist()
