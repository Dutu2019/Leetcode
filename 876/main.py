import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return str(self.val)

l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

def middleNode(l: ListNode) -> ListNode:
    currNode = l
    counter = 1
    while currNode.next:
        currNode = currNode.next
        counter += 1
    
    index = math.floor(counter/2)
    for i in range(index):
        l = l.next
    return l

print(middleNode(l))
