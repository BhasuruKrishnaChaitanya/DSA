from .upper_bound import upper_bound
from .lower_bound import lower_bound

def first_and_last_occurance(arr, target):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def first_and_last_occurance(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('first_and_last_occurance') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    lb = lower_bound(arr, target)
    if lb > len(arr) - 1 or arr[lb] != target:
        return [-1, -1]
    ub = upper_bound(arr, target)
    if ub == 0:
        return [lb, lb]
    return [lb, ub-1]