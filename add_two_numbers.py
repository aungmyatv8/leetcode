class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  
    current = dummy  
    carry = 0


    while l1 or l2 or carry:
        sum_val = carry 
        if l1:
            print(l1.val, sum_val)
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        carry = sum_val // 10
        digit = sum_val % 10

        current.next = ListNode(digit)
        current = current.next
        # print(current.next)

    return dummy.next  

# Create linked lists l1 and l2
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Call the addTwoNumbers function and print the result
result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
