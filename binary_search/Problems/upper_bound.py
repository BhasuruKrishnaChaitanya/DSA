def upper_bound(arr, target):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def upper_bound(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('upper_bound') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    def recursive(arr, target, low, high, index):
        if low > high:
            return index
        if target >= arr[(low + high) // 2]:
            return recursive(arr, target, ((low + high) // 2) + 1, high, index)
        else:
            return recursive(arr, target, low, ((low + high) // 2) - 1, ((low + high) // 2))

    index = len(arr)
    return recursive(arr, target, 0, len(arr) - 1, index)