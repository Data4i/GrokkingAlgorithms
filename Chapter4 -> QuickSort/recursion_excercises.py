# Write out a recursive code to sum numbers in an array
def sum_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum_arr(arr[1:])


print(sum_arr([2, 3, 4]))
print(sum_arr([3]))
print(sum_arr([]))


# Write out a recursive function to count the number of items in a list
def count_arr(arr):
    if not arr:
        return 0
    return 1 + count_arr(arr[1:])


print(count_arr([1, 2, 3, 4, 5, 3, 3, 3]))
print([1, 2, 3, 4, 5, 3, 3, 3][1:])


def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max_num([1, 2, 3, 4, 5, 3, 3, 3]))


# Write out a recursive function for the binary search done in chapter 1
def recursive_binary_search(arr, item):
    if not arr:
        return None
    index = int((len(arr)) / 2)
    if arr[index] == item: return index

    if arr[index] > item: return recursive_binary_search(arr[:index], item)

    if arr[index] < item: return recursive_binary_search(arr[index + 1:], item) + len(arr[:index + 1])


fruits = ['apple', 'banana', 'carrot', 'cucumber', 'mango', 'pawpaw', 'watermelon']
item_index = recursive_binary_search(fruits, 'pawpaw')
print(f'Function Item Index: {item_index}, Fruit: {fruits[item_index]}')


# Use quick sort algorithm to sort an array
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if pivot >= i]
        greater = [i for i in arr[1:] if pivot < i]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 4, 52, 3, 7, 1, 99, 0]))
