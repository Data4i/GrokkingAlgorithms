def binary_search(array, item):
    """
    Running time: O(log base 2 n)


    :param array: The Array to be searched
    :param item: The Item to be searched for
    :return: The index of the Item searched for else None
    """

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + high
        guess = array[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


fruits = sorted(['apple', 'banana', 'mango', 'pawpaw', 'watermelon', 'cucumber', 'carrot'])
item_index = binary_search(fruits, 'mango')
print(f'Sorted Fruits: {fruits}')
print(f'Function Item Index: {item_index}, Fruit: {fruits[item_index]}')

