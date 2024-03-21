from merge_sort import merge_sort


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def sort(self):
        lst = []
        cur = self.head
        while cur:
            lst.append(cur.data)
            self.delete_node(cur.data)
            cur = cur.next
        lst = merge_sort(lst)

        for data in lst[::-1]:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def merge(self, second):
        first = self.head
        second = second.head
        if not first:
            return second
        if not second:
            return first

        if first.data <= second.data:
            temp = first
            first = temp.next
        else:
            temp = second
            second = temp.next
        node = temp
        while first and second:
            if first.data <= second.data:
                temp.next = first
                temp = first
                first = temp.next
            else:
                temp.next = second
                temp = second
                second = temp.next
        if not first:
            temp.next = second
        if not second:
            temp.next = first
        return node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            if cur is None:
                return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)
llist.sort()
# llist.reverse()
print("Зв'язний список:")
llist.print_list()

llist_2 = LinkedList()

llist_2.insert_at_beginning(3)
llist_2.insert_at_beginning(8)
llist_2.insert_at_beginning(16)
llist_2.insert_at_end(22)
llist_2.insert_at_end(27)
llist_2.sort()

llist.merge(llist_2)
print("Зв'язний список:")
llist.print_list()
