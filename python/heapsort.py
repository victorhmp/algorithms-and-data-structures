# Heapsort is another sorting algorithm that can run on O(n log n) time.
# Different from quicksort, heapsort sorts *in place*, so only a constant
# number of array elements are stored outside the input array at any time.
from heap import MaxHeap


# One thing I don't particularly like about this implementation is that,
# internally, it kinda breaks the heap that is created, and also accesses
# some properties directly. But it's easier to write and get the idea.
def heap_sort(input_array):
    heap = MaxHeap(input_array, len(input_array))

    for i in range(len(input_array), 1, -1):
        # Here I'm just taking advantage of the fact that the root of the heap
        # is always its biggest element.
        heap.items[1], heap.items[i] = heap.items[i], heap.items[1]

        heap.heap_size -= 1
        heap.max_heapify(1)

    return heap.items[1:]


if __name__ == "__main__":
    input_array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heap_sort(input_array))
