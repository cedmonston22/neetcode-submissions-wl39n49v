class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.head = None  # Next
        self.tail = None  # Previous


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}

        self.head = Node()
        self.tail = Node()
        self.head.head = self.tail
        self.tail.tail = self.head

    def remove(self, node):
        previous = node.tail
        next_node = node.head

        previous.head = next_node
        next_node.tail = previous

    def insert(self, node):
        first = self.head.head

        node.tail = self.head
        node.head = first
        self.head.head = node
        first.tail = node

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return

        node = Node(key, value)
        self.d[key] = node
        self.insert(node)

        if len(self.d) > self.capacity:
            oldest = self.tail.tail
            self.remove(oldest)
            del self.d[oldest.key]