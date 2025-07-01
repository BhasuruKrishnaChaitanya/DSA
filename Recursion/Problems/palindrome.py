def palindrome(s):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def palindrome(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('palindrome') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    def two_pointer(s, l, r):
        if l > r:
            return True
        return (s[l] == s[r]) and (two_pointer(s, l+1, r-1))
    
    return two_pointer(s, 0, len(s) - 1)