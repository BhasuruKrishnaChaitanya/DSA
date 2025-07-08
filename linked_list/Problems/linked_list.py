class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return ", ".join(map(str, elements))
    
    def length(self):
        n = 0
        current = self.head
        while current:
            n += 1
            current = current.next
        return n
    
    def find(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def update(self, target, value):
        # This implementation updates ALL occurrences of the target.
        current = self.head
        while current:
            if current.data == target:
                current.data = value
            current = current.next

    def deletek(self, index):
        # This implementation uses 0-based indexing.
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            return
        n = 0
        prev = None
        current = self.head
        while current is not None and n < index:
            prev = current
            current = current.next
            n += 1
        
        if current is None:
            return
        
        prev.next = current.next
    
    def deleteT(self, target):
        # This implementation deletes the FIRST occurrence of the target.
        if self.head == None:
            return
        if self.head.data == target:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        while current is not None and current.data != target:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next

# --- Test Harness Function ---
# This is the main function that your test_runner will call.
def linked_list(initial_list, operations):
    """
    This function acts as a test harness for the LinkedList class.
    It first initializes a list with `initial_list`.
    Then, it performs a series of `operations` on the list.
    Finally, it returns a dictionary containing key results for verification.
    """
    
    # 1. Initialize the LinkedList with the starting data
    ll = LinkedList()
    for item in initial_list:
        ll.insert(item)
    
    # This will store results from specific operations like 'find'
    operation_results = []

    # 2. Perform the sequence of operations
    for op in operations:
        command = op[0]
        args = op[1:]

        if command == "insert":
            ll.insert(*args)
        elif command == "deletek":
            ll.deletek(*args)
        elif command == "deleteT":
            ll.deleteT(*args)
        elif command == "update":
            ll.update(*args)
        elif command == "find":
            # For operations that return a value, we store the result
            result = ll.find(*args)
            operation_results.append(result)

    # 3. Return a dictionary of final results to be tested
    return {
        "final_list": ll.display(),
        "final_length": ll.length(),
        "operation_results": operation_results
    }
