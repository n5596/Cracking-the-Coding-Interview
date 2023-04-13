class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = None
        self.tail = None

    def remove_node(self, node):
        # removing this node from the list
        
        if node == None:
            return 
                
        if node.prev != None: # node is not the head
            node.prev.next = node.next
            
        if node.next != None: # node is not the tail
            node.next.prev = node.prev
        
        if node == self.tail:
            self.tail = self.tail.prev
        if node == self.head:
            self.head = self.head.next
            
        return
    
    def insert_in_front(self, node):
        # adding it to the head
        
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        self.head.prev = node
        node.next = self.head
        
        node.prev = None
        self.head = node
        return
    
    def remove_key(self, key):
        if key not in self.dict:
            return
        
        node = self.dict[key]
        self.remove_node(node)
        del self.dict[key]
        return
        
    def get(self, key: int) -> int:
                
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        
        if node == self.head: # it's already in the front
            return node.val
        
        self.remove_node(node)
        self.insert_in_front(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        
        self.remove_key(key)
        
        if len(self.dict.keys())+1 > self.capacity: # over capacity
            self.remove_key(self.tail.key)
            
        new_node = Node(key, value)

        self.insert_in_front(new_node)        
        self.dict[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
