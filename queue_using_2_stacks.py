# Queue using 2 Stacks
from stack import Stack
stack1 = Stack()
stack2 = Stack()

class Queue(Stack):
    
    def enqueue(self,item):
        stack1.push(item)
        # stack1.print_stack()

    def dequeue(self):
        if not stack2.is_empty():
            popped = stack2.pop()
            return popped
        else:
            while not stack1.is_empty():
                stack2.push(stack1.pop())
            popped = stack2.pop()
            return popped

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())

