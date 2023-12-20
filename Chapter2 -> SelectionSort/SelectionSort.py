def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    f"""
    Running time: O(n * n) -> O(n**2)
    :param arr: Array/list to be sorted
    :return: Sorted Array/List
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 1, 9, 2, 3, 9, 0, 4]))
