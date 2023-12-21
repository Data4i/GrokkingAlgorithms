# Write out a recursive code to sum numbers in an array
def sum_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])


print(sum_arr([2, 3, 4]))
print(sum_arr([3]))
print(sum_arr([]))


# Write out a recursive function to count the number of items in a list
def count_arr(arr):
    if not arr:
        return 0
    return 1 + count_arr(arr[1:])


print(count_arr([1, 2, 3, 4, 5, 3, 3, 3]))
