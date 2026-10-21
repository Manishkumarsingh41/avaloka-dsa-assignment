class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        self.capacity = capacity
        self.items = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_first(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.items:
            return -1

        node = self.items[key]
        self.remove(node)
        self.add_first(node)

        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.items:
            node = self.items[key]
            node.value = value
            self.remove(node)
            self.add_first(node)
            return

        if len(self.items) == self.capacity:
            old_node = self.tail.prev
            self.remove(old_node)
            del self.items[old_node.key]

        node = Node(key, value)
        self.items[key] = node
        self.add_first(node)
