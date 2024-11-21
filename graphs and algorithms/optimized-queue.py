class OptimizedQueue:
    def __init__(self):
        self.queue = []
        self.num_operations = 0  # Keeps track of number of operations to calculate amortized cost
    
    def enqueue(self, item):
        self.queue.append(item)
        self.num_operations += 1
        # Occasionally, move elements to the front
        if len(self.queue) % 5 == 0:  # Assume we move every 5 operations (for simplicity)
            self.move_elements_to_front()
    
    def dequeue(self):
        if not self.is_empty():
            self.num_operations += 1
            return self.queue.pop(0)
        else:
            return None
    
    def move_elements_to_front(self):
        # Simulating the costly operation: Move all elements to the front
        print("Moving elements to the front (expensive operation)")
        self.queue = self.queue[::-1]  # Reverses the queue to simulate a move to the front
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def get_queue(self):
        return self.queue

# Simulate the queue operations
queue = OptimizedQueue()
for i in range(15):
    queue.enqueue(i)  # Enqueue operations
    
print(f"Queue after 15 operations: {queue.get_queue()}")
