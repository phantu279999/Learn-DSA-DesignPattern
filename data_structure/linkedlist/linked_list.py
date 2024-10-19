class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def insert_position(self, position, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        elif position == -1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            c = 0
            temp = self.head
            while c < position:
                c += 1
                temp = temp.next

            next_node = temp.next
            temp.next = new_node
            new_node.next = next_node

    def delete_position(self, position):
        if self.head is None:
            print('Linked list is empty!')
            return

        if position == 0:
            self.head = self.head.next
            return
        elif position == -1:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next

            prev.next = None
            self.tail = prev
        else:
            temp = self.head
            prev = None
            c = 0
            while c < position:
                c += 1
                prev = temp
                temp = temp.next

            prev.next = temp.next

    def delete_duplicates(self):
        store = []
        temp = self.head
        prev = None
        while temp:
            if temp.data not in store:
                store.append(temp.data)
                prev = temp
            else:
                prev.next = temp.next
            temp = temp.next

    @staticmethod
    def merge_two_lists(l1, l2):
        temp_1 = l1
        temp_2 = l2
        new_lists = LinkedList()

        while temp_1 and temp_2:
            if temp_1.data < temp_2.data:
                new_lists.append(temp_1.data)
                temp_1 = temp_1.next
            else:
                new_lists.append(temp_2.data)
                temp_2 = temp_2.next

        while temp_1:
            new_lists.append(temp_1.data)
            temp_1 = temp_1.next

        while temp_2:
            new_lists.append(temp_2.data)
            temp_2 = temp_2.next

        return new_lists

    def reverse_linkedlist(self):
        cur_node = self.head
        prev = None
        while cur_node is not None:
            temp = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = temp

        self.head = prev

    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        return count

    def middle_element_of_linkedlist(self):
        n = 0
        store = []
        temp = self.head
        while temp:
            n += 1
            store.append(temp.data)
            temp = temp.next

        return store[n // 2]

    def has_loop(self):
        visited = []
        temp = self.head
        while temp:
            if id(temp) not in visited:
                visited.append(id(temp))
            else:
                return True
            temp = temp.next

        return False

    def is_palindrome(self):
        if self.head is None:
            return True

        store = []
        temp = self.head
        while temp:
            store.append(temp.data)
            temp = temp.next

        if store == store[::-1]:
            return True
        return False

    def traversal_linkedlist(self):
        temporary = self.head
        while temporary is not None:
            print(temporary.data, end=" ")
            temporary = temporary.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(1)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.append(3)
    ll.append(4)
    ll.append(4)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.traversal_linkedlist()
    ll.delete_duplicates()
    ll.traversal_linkedlist()
