import heapq
from collections import defaultdict

# Class to represent a node in the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # To make Node comparable, so it can be used in a priority queue (heap)
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freqs):
    # Create a priority queue (min heap)
    heap = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Take two nodes with the smallest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new internal node with the sum of frequencies
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        
        # Add the new node back to the priority queue
        heapq.heappush(heap, internal_node)
    
    # The remaining node is the root of the Huffman tree
    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        # If it's a leaf node, assign the code
        if node.char is not None:
            codebook[node.char] = prefix
        # Recurse for left and right subtrees
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# Example usage:
if __name__ == "__main__":
    # Character frequencies
    freqs = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    
    # Build the Huffman tree
    root = build_huffman_tree(freqs)
    
    # Generate the Huffman codes
    huffman_codes = generate_codes(root)
    
    # Output the Huffman codes
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
