def oneToNBacktracking(n):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def oneToNBacktracking(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('oneToNBacktracking') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    if n <= 0:
        return []
    return oneToNBacktracking(n-1) + [n]