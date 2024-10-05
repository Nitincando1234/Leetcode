class Node:
    def __init__(self, key = 0, value = 0):
        self.key, self.value = key, value
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(self.left.next)
            del self.cache[lru.key]
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        node.next, node.prev = nxt, prev
        prev.next, nxt.prev = node.next, node.prev
    
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        prev.next, nxt.prev = node, node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)