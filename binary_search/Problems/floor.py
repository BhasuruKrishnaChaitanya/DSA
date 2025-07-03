from .upper_bound import upper_bound
def floor(arr, target):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def floor(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('floor') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    idx = upper_bound(arr, target)
    if idx == 0:
        return -1
    return arr[idx - 1]