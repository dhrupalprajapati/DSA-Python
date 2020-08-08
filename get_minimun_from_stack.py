# use 2 stack 1. Original stack & 2. Supporting stack for Minimum stack

from stack import Stack

stack = Stack()
support_stack = Stack()

class  MinStack:
    def push(self,item):
        if stack.is_empty():
            stack.push(item)
            support_stack.push(item)
        else:
            stack.push(item)
            if (stack.peek() < support_stack.peek()):
                support_stack.push(item)
            
    def pop(self):
        if not stack.is_empty():
            if stack.peek() == support_stack.peek():
                stack.pop()
                support_stack.pop()
            else:
                stack.pop()

    def get_min(self):
        if not support_stack.is_empty():
            return support_stack.peek()

s = MinStack()
s.push(10)
s.push(3)
s.push(4)
s.pop()
s.pop()
s.push(12)
s.push(8)
s.push(9)
print(stack.printStack(), support_stack.printStack())
