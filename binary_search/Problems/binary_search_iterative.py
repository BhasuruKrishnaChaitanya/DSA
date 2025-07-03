def binary_search_iterative(arr, target):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def binary_search_iterative(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('binary_search_iterative') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False