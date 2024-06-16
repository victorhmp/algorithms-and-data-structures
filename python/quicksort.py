# The most interesting part about quicksort is not so much its implementation,
# but the mathematical analysis of its running time. In specific, how the
# introduction of randomness in the choice of the pivot element can lead to
# better expected running times.
#
# It's also interesting that quicksort actually has a worst-case running time
# worse then both heapsort and mergesort, but it's still the most used sorting
# algorithm in practice. Although, in practice, its implementation does include
# randomness in the choice of the pivot for partitions and further optimization
# specific to the library of language that implements it.


def quicksort(input_array, low, high):
    if low < high:
        pivot_index = partition(input_array, low, high)
        quicksort(input_array, low, pivot_index - 1)
        quicksort(input_array, pivot_index + 1, high)


# Important to note that the input_array is rearrenged in place.
# The partition here will rearrange the array in such a way that two subarrays
# are created: A[low:pivot-1] (low size) and A[pivot+1:high] (high side).
# A[pivot] is greater than all elements in the low side and smaller than (or
# equal to) all elements in the high side.
def partition(arr, low, high):
    pivot = arr[high]
    highest_low_side_index = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            highest_low_side_index += 1
            arr[highest_low_side_index], arr[j] = arr[j], arr[highest_low_side_index]

    # This line places the pivot in its place. Right after highest_low_side_index.
    arr[highest_low_side_index + 1], arr[high] = (
        arr[high],
        arr[highest_low_side_index + 1],
    )

    return highest_low_side_index + 1


if __name__ == "__main__":
    input_array = [2, 8, 7, 1, 3, 5, 6, 4]
    quicksort(input_array, 0, 7)

    print(input_array)
