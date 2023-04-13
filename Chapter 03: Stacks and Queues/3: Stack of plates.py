class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = [[]]
        self.heap = []

    def push(self, val: int) -> None:
        
        while len(self.heap) > 0 and self.heap[0] >= len(self.stacks):
            heapq.heappop(self.heap)
            
        if self.heap == []:
            if len(self.stacks[-1]) >= self.capacity: # cannot push
                self.stacks.append([])
            idx = -1
        else:
            idx = self.heap[0]
            heapq.heappop(self.heap)

        self.stacks[idx].append(val)

    def pop(self) -> int:
        while self.stacks != [] and self.stacks[-1] == []: # getting rid of empty right stacks
            self.stacks.pop()
        
        if self.stacks == []:
            return -1
        
        val = self.stacks[-1].pop()
        return val

    def popAtStack(self, index: int) -> int:
        if len(self.stacks) < index or self.stacks[index] == []:
            return -1
        val = self.stacks[index].pop()
        
        heapq.heappush(self.heap, index)
        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
