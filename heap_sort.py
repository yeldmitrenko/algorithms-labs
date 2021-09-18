import time

compare_count = 0
swap_count = 0


def heapify(array, current_index, heap_size, sort_order):
    global compare_count
    global swap_count

    largest_element = current_index
    left_child = 2 * current_index + 1
    right_child = 2 * current_index + 2

    def compare(a, b):
        if a >= b:
            return 1
        else:
            return -1

    if left_child < heap_size and compare(array[left_child], array[current_index]) != compare(sort_order, "desc"):
        largest_element = left_child
    compare_count += 4

    if right_child < heap_size and compare(array[right_child], array[largest_element]) != compare(sort_order, "desc"):
        largest_element = right_child
    compare_count += 4

    if largest_element != current_index:
        array[current_index], array[largest_element] = array[largest_element], array[current_index]
        compare_count += 1
        swap_count += 1
        heapify(array, current_index, heap_size, sort_order)


def heap_sort(array, sort_order):
    global swap_count

    array_length = len(array)
    for i in range(array_length // 2, -1, -1):
        heapify(array, i, array_length, sort_order)

    for i in range(array_length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i, sort_order)
    swap_count += 1

    return array


def main():
    global swap_count
    global compare_count

    sort_order = str(input("Enter sort order (asc or desc): "))
    array = [int(item) for item in input("Enter initial array: ").split(",")]

    start_time = time.perf_counter()
    heap_sort(array, sort_order)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    print(f"Execution time: {execution_time} ms")

    print(f"Comparisons: {compare_count}")
    print(f"Swaps: {swap_count}")

    print("Heap sort:", heap_sort(array, sort_order))
