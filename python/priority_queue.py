# Here we're using MaxHeap to serve as the basis for a MaxPriorityQueue, and
# that makes it possible to support any operations in O(lg n), plus the
# overhead to maintain references from keys in the heap to actual objects
# in the queue.
from heap import MaxHeap
import math


class MaxPriorityQueue(MaxHeap):
    def __init__(self, input_array, size):
        self.keys_map = dict()
        self.keys = []
        for item in input_array:
            self.keys_map[item["key"]] = item
            self.keys.append(item["key"])

        super().__init__(self.keys, size)

    def heap_maximum(self):
        if self.heap_size < 1:
            raise ValueError("Heap underflow")

        return self.items[1]

    def extract_max(self):
        # The call to max_heapify and the use of self.items is assuming
        # that the MaxHeap only contains numbers and manipulates their indexes
        # in an array. The notion of 'objects' with 'priorities' is unknown to
        # the MaxHeap, but essencial here in this class.
        max = self.heap_maximum()
        self.items[1] = self.items[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)

        return max

    def increase_key(self, obj, new_key):
        original_key = obj["key"]
        if new_key < original_key:
            raise ValueError("Decreasing a key is not supported.")

        # Keep consistence between heap and objects.
        self.keys_map[new_key] = obj
        self.keys_map.pop(original_key)

        obj_index = 0
        for i in range(1, len(self.items)):
            if self.items[i] == original_key:
                obj_index = i
                obj.update({"key": new_key})
                self.items[i] = new_key

        while (
            obj_index > 1 and self.items[self.parent(obj_index)] < self.items[obj_index]
        ):
            self.items[obj_index], self.items[self.parent(obj_index)] = (
                self.items[self.parent(obj_index)],
                self.items[obj_index],
            )

            obj_index = self.parent(obj_index)

    def insert(self, obj):
        self.heap_size += 1
        new_key = obj["key"]
        obj["key"] = -math.inf

        self.items.append(obj["key"])
        self.keys_map[obj["key"]] = obj

        self.increase_key(obj, new_key)


if __name__ == "__main__":
    input_array = [
        {"key": 16, "message": "something1"},
        {"key": 14, "message": "something2"},
        {"key": 10, "message": "something3"},
        {"key": 8, "message": "something4"},
        {"key": 7, "message": "something5"},
        {"key": 9, "message": "something6"},
        {"key": 3, "message": "something7"},
        {"key": 2, "message": "something8"},
        {"key": 4, "message": "something9"},
        {"key": 1, "message": "something0"},
    ]

    queue = MaxPriorityQueue(input_array, 10)

    print("this is the max " + str(queue.heap_maximum()))
    queue.increase_key(input_array[8], 15)

    print(queue)
    print(queue.insert({"key": 22, "message": "something5"}))
    print(queue)
