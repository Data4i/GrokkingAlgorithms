def sum_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])


print(sum_arr([2, 3, 4]))
print(sum_arr([3]))
print(sum_arr([]))

