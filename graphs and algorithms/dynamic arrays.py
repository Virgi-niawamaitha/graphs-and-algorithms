class DynamicArray:
    def __init__(self):
        self.array = []
        self.capacity = 1  # Initial capacity
        self.size = 0
        self.total_cost = 0
        self.resize_count = 0

    def insert(self, value):
        # Check if resizing is needed
        if self.size == self.capacity:
            self._resize()

        # Insert the new value
        self.array.append(value)
        self.size += 1
        self.total_cost += 1  # Increment cost for the insertion

    def _resize(self):
        # Double the capacity and account for resizing cost
        self.capacity *= 2
        self.resize_count += 1
        self.total_cost += self.size  # Cost of copying elements to the new array

    def amortized_cost(self):
        return self.total_cost / self.size if self.size > 0 else 0

# Simulating post insertions
dynamic_array = DynamicArray()
posts = ["Post1", "Post2", "Post3", "Post4", "Post5", "Post6"]

for post in posts:
    dynamic_array.insert(post)

print("Total operations cost:", dynamic_array.total_cost)
print("Total number of insertions:", dynamic_array.size)
print("Amortized cost per insertion:", dynamic_array.amortized_cost())
print("Number of resizes:", dynamic_array.resize_count)
