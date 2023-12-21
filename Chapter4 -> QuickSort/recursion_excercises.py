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
