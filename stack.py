class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def is_empty(self):
        return self.stack == []
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def print_stack(self):
        print(*self.stack)
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.peek())
# print(s.pop())
# print(s.peek())