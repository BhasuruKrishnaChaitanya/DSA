def reverse_array(arr):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def reverse_array(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('reverse_array') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    def two_pointer(arr, l, r):
        if l >= r:
            return arr
        arr[l] = arr[l] + arr[r]
        arr[r] = arr[l] - arr[r]
        arr[l] = arr[l] - arr[r]
        return two_pointer(arr, l+1 , r-1)
    return two_pointer(arr, 0, len(arr)-1)
    # if arr == []:
    #     return []
    # return [arr.pop()] + reverse_array(arr)