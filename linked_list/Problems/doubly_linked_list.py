class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return ", ".join(map(str, elements))
    
    def display_reverse(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
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
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        current = self.head
        n = 0
        while current is not None and n < index:
            current = current.next
            n += 1
        
        if current is None:
            return
        
        prev_node = current.prev
        prev_node.next = current.next
        
        if current.next:
            current.next.prev = prev_node
        else:
            self.tail = prev_node

    def deleteT(self, target):
        # This implementation deletes the FIRST occurrence of the target.
        current = self.head
        while current is not None and current.data != target:
            current = current.next
        
        if current is None:
            return
            
        prev_node = current.prev
        if prev_node:
            prev_node.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = prev_node
        else:
            self.tail = prev_node
    
    def reverse(self):
        # If the list is empty or has only one node, there's nothing to do.
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current:
            # Swap the prev and next pointers for the current node
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            current = current.prev

        # After the loop, the roles of head and tail are swapped.
        # We can do this with a simple swap.
        temp = self.head
        self.head = self.tail
        self.tail = temp



# --- Test Harness Function ---
def doubly_linked_list(initial_list, operations):
    """Test harness for the DoublyLinkedList class."""
    ll = DoublyLinkedList()
    for item in initial_list:
        ll.insert(item)
    
    operation_results = []

    # Inside the doubly_linked_list_operations function...
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
            result = ll.find(*args)
            operation_results.append(result)
        # Add this new case for the reverse operation
        elif command == "reverse":
            ll.reverse()

    return {
        "final_list": ll.display(),
        "final_list_reverse": ll.display_reverse(),
        "final_length": ll.length(),
        "operation_results": operation_results
    }
