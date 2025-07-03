def binary_search_recursive(arr, target):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def binary_search_recursive(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('binary_search_recursive') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    def recursive(arr, target, low, high):
        if low > high:
            return False
        if target == arr[(low + high) // 2]:
            return True
        elif target > arr[(low + high) // 2]:
            return recursive(arr, target, ((low + high) // 2) + 1, high)
        else:
            return recursive(arr, target, low, ((low + high) // 2) - 1)

    return recursive(arr, target, 0, len(arr) - 1)