# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base condition
    if end >= start:

        # finds the middle of the array - // 2 would round down any intger numbers
        middle = (start + end) // 2

        # returns middle if it's equal to target
        if target == arr[middle]:
            return middle

        # removes all values from the right side including middle
        # if target value is smaller than middle
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)

        # otherwise target must be on the right side of middle
        # removes all values from the left side including middle
        else:
            return binary_search(arr, target, middle + 1, end)
    else:
        # if value isn't in the array
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
