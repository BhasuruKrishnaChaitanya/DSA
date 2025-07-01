def name5Times(name, n=0, result_list=None):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def name5Times(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('name5Times') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    if result_list is None:
        result_list = []
    if n >= 5:
        return result_list
    result_list.append(name)
    return name5Times(name, n + 1, result_list)