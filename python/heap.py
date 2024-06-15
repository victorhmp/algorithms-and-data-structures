# A heap in its most useful application is a priority queue.
# It is an array object that can be viewed as a nearly complete binary tree.
# It's also cool to notice that `parent`, `left` and `right` are all simple
# binary operations, so they can be optimized as inline procedures or macros.

# There are two types of heaps: max-heaps and min-heaps.
# Each of them maintains a specific "heap property" that correspoonds to the
# desired order of the elements in the heap.

# Two general binary tree property also valid for heaps:
# - A heap of n elements has height O(lg n).
# - Basic operations run in time at most proportional to the height of the tree.


# Note: this heap is 1-indexed.
class MaxHeap:
    def __init__(self, input_array, size):
        self.items = [None] + input_array
        self.heap_size = size

        # The loop invariant we're assuming here is that:
        # At the start of each iteration, each node i+1, i+2, ..., n is the
        # root of a max-heap. At the end, when i would be zero, all elements
        # 1, 2, 3, ..., n are the root of a max-heap.
        # This is also anchored at the fact that elements items[n//2 + 1:n] are
        # all leaves of the tree. That's why we can start at n//2 and go down.
        for i in range(size // 2, 0, -1):
            self.max_heapify(i)

        return

    def __str__(self):
        return str(self.items[1:])

    def parent(self, index):
        return index // 2

    def left(self, index):
        return 2 * index

    def right(self, index):
        return 2 * index + 1

    # This is the most interesting method of the class.
    # It checks for the heap property, starting at `index` and fixes the heap
    # if it needs to, recursively. Also of note is that the recursive calls
    # move "down" the tree.
    def max_heapify(self, index):
        left_index = self.left(index)
        right_index = self.right(index)

        largest_element_index = index

        if left_index <= self.heap_size and self.items[left_index] > self.items[index]:
            largest_element_index = left_index

        if (
            right_index <= self.heap_size
            and self.items[right_index] > self.items[largest_element_index]
        ):
            largest_element_index = right_index

        # This is basically just checking to see if we actually changed something.
        # If so, we swap the elements and call max_heapify again.
        if largest_element_index != index:
            # This is pretty neat thing to do in Python, you can just swap
            # values without needing a temporary variable.
            self.items[index], self.items[largest_element_index] = (
                self.items[largest_element_index],
                self.items[index],
            )
            self.max_heapify(largest_element_index)

        return


my_heap = MaxHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], 10)
my_other_heap = MaxHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)

print(my_other_heap)
print(my_heap)
