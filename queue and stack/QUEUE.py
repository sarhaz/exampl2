class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(2)
queue.enqueue("SARDOR")
queue.enqueue(4)
queue.enqueue("BAHODIR")
queue.enqueue(6)
queue.enqueue("RUSLAN")
print(queue.items)


for i in queue.items:
    print(i)

a = queue.size()
print("LENGTH OF QUEUE: ", a)