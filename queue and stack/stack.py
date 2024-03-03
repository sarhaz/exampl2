class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)


stack = Stack()

print("--------PUSH---------")
stack.push(2)
stack.push(4)
stack.push(6)
stack.push(8)
stack.push(10)
stack.push(12)
stack.push(14)

print("--------POP---------")
stack.pop()
stack.pop()
stack.pop()

for i in stack.items:
    print(i)

print("--------SIZE---------")
a = stack.size()
print("length of the stack: ", a)
