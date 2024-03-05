class Node:
    '''
    node of doubly linked list
    '''
    def __init__(self, key=0, value=0) -> None:
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    '''
    1. Using the hashmap as a node pool, alose provide $O(1)$ get and put.
    2. Using a doubly linked list as LRU list, left most node as LRU, right
    most node as most recent used.
    ```
    +------+     +-----+             +------------------+     +-------+
    | left | <=> | LRU | <=> ... <=> | most recent used | <=> | right |
    +------+     +-----+             +------------------+     +-------+
    ```
    3. Store key in both list node and hashmap to provide two-way map.
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recent used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # remove the LRU
        if len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
    
    def insert(self, node: Node):
        '''
        insert to the next of right (a.k.a most recent used).
        '''
        old = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = old
        old.next = node
    
    def remove(self, node: Node):
        '''
        remove a node from a doubly linked list.
        '''
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev = node.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)