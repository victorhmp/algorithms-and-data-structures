class Node:
    def __init__(self, data: str, key: int):
        self.data = data
        self.key = key
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self):
        return f"Node(key={self.key}, data={self.data}, next={self.next != None}, prev={self.prev != None})"


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def search(self, key):
        x = self.head
        while x != None and x.key != key:
            x = x.next

        if x == None:
            raise ValueError("key not found")

        return x

    # This is one of the methods that justify the use of a linked list, since
    # it's O(1) time complexity.
    def prepend(self, data, key):
        new_node = Node(data, key)
        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node

        self.head = new_node

    # This one is also better than the array implementation.
    def append(self, data, key):
        new_node = Node(data, key)
        new_node.next = None
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node
        if self.head == None:
            self.head = new_node

    def insert_after(self, data, key, after_key):
        new_node = Node(data, key)

        x = self.search(after_key)
        new_node.next = x.next
        new_node.prev = x

        if x.next != None:
            x.next.prev = new_node
        else:
            self.tail = new_node

        x.next = new_node

    def delete(self, key):
        node_to_delete = self.search(key)

        if node_to_delete.prev != None:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next

        if node_to_delete.next != None:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.tail = node_to_delete.prev


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append("first", 1)
    linked_list.append("second", 2)
    linked_list.append("third", 3)
    linked_list.insert_after("fourth", 4, 2)
    linked_list.delete(2)

    x = linked_list.head
    while x != None:
        print(x)
        x = x.next
