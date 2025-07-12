from .linked_list import Node, LinkedList

def add_two_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    dummy_head = Node(0)
    current = dummy_head
    carry = 0
    
    p1 = l1.head
    p2 = l2.head

    while p1 is not None or p2 is not None or carry != 0:
        val1 = p1.data if p1 is not None else 0
        val2 = p2.data if p2 is not None else 0
        
        total_sum = val1 + val2 + carry
        digit = total_sum % 10
        carry = total_sum // 10
        
        current.next = Node(digit)
        current = current.next
        
        p1 = p1.next if p1 is not None else None
        p2 = p2.next if p2 is not None else None
        
    result_list = LinkedList()
    result_list.head = dummy_head.next
    return result_list


# --- Test Harness Function ---
# This is the function your test_runner will call.
def add_numbers(arr1, arr2):
    # 1. Create the two input linked lists
    list1 = LinkedList()
    for item in arr1:
        list1.insert(item)

    list2 = LinkedList()
    for item in arr2:
        list2.insert(item)

    # 2. Call the main logic function
    result_list = add_two_numbers(list1, list2)

    # 3. Return the result as a string for easy comparison
    if result_list and result_list.head:
        return result_list.display()
    return ""
