class Stack:

    def __init__(self, items = None, limit = 100):
        if items is None:
            items = []
        self.items = list(items) 
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if len(self.items) >= self.limit:
            return None
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
            # raise Exception("Stack underflow")
        return self.items.pop()
        
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            return self.items[::-1].index(target)
        except ValueError:
            return -1